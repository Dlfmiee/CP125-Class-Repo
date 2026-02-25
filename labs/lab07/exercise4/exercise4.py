def apply_upgrade(current, upgrade):

    result = dict(current)

    for perm, level in upgrade.items():
        if perm not in result:
            result[perm] = level
        else:
            if level > result[perm]:
                result[perm] = level

    return result



current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}
result = apply_upgrade(current, upgrade)
print(result)
print(current)   # Should be unchanged
