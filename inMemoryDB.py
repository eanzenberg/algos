class inMemoryDB:
    def __init__(self):
        self.db = {}
        self.backups = {}

    def set(self, key: str, field: str, value: str) -> None:
        if key not in self.db:
            self.db[key] = {}
        self.db[key][field] = value

    def get(self, key: str, field: str) -> str | None:
        return self.db.get(key, {}).get(field, None)

    def delete(self, key: str, field: str) -> bool:
        if key in self.db and field in self.db[key]:
            del self.db[key][field]
            if not self.db[key]:
                del self.db[key]
            return True
        return False

    def scan(self, key: str) -> list[str]:
        if key not in self.db:
            return []
        return [f"{f}({self.db[key][f]})" for f in sorted(self.db[key].keys())]

    def scan_by_prefix(self, key: str, prefix: str) -> list[str]:
        if key not in self.db:
            return []
        fields_with_prefix = [f for f in self.db[key] if f.startswith(prefix)]
        return [f"{f}({self.db[key][f]})" for f in sorted(fields_with_prefix)]

    def _set_field(self, key, field, value, timestamp, ttl):
        if key not in self.db:
            self.db[key] = {}
        self.db[key][field] = {"value": value, "timestamp": timestamp, "ttl": ttl}

    def set_at(self, key: str, field: str, value: str, timestamp: int) -> None:
        self._set_field(key, field, value, timestamp, None)

    def set_at_with_ttl(self, key: str, field: str, value: str, timestamp: int, ttl: int) -> None:
        self._set_field(key, field, value, timestamp, ttl)

    def get_at(self, key: str, field: str, timestamp: int) -> str | None:
        field = self.db.get(key, {}).get(field)
        if field and self._valid_time(field, timestamp):
            return field['value']
        return None

    def scan_by_prefix_at(self, key: str, prefix: str, timestamp: int) -> list[str]:
        if key not in self.db:
            return []
        return [f"{field}({info['value']})" for field, info in sorted(self.db[key].items()) if field.startswith(prefix) and self._valid_time(info, timestamp)]

    def delete_at(self, key: str, field: str, timestamp: int) -> bool:
        if key in self.db and field in self.db[key] and self._valid_time(self.db[key][field], timestamp):
            del self.db[key][field]
            if not self.db[key]:
                del self.db[key]
            return True
        return False

    def scan_at(self, key: str, timestamp: int) -> list[str]:
        if key not in self.db:
            return []
        return [f"{field}({info['value']})" for field, info in sorted(self.db[key].items()) if self._valid_time(info, timestamp)]

    def backup(self, timestamp: int) -> int:
        records = 0
        backup = {}
        for k, fields in self.db.items():
            backup[k] = {}
            for f, data in fields.items():
                if self._valid_time(data, timestamp):
                    if data["ttl"] is not None:
                        remaining_ttl = data["ttl"] - (timestamp - data["timestamp"])
                    else:
                        remaining_ttl = None
                    backup[k][f] = {"value": data["value"], "timestamp": data["timestamp"], "ttl": remaining_ttl}
                records += 1
        self.backups[timestamp] = backup
        return records

    def _valid_time(self, field_info, timestamp):
        ttl = field_info['ttl'] if field_info['ttl'] is not None else float('inf')
        return field_info['timestamp'] <= timestamp < (field_info['timestamp'] + ttl)

    def restore(self, timestamp: int, timestamp_to_restore: int) -> None:
        last_backup_time = max(t for t in self.backups if t <= timestamp_to_restore)
        restored_backup = self.backups[last_backup_time]
        self.db.clear()
        for k, field in restored_backup.items():
            self.db[k] = {}
            for f, data in field.items():
                self.db[k][f] = {
                    "value": data["value"],
                    "timestamp": timestamp,
                    "ttl": data["ttl"]
                }
