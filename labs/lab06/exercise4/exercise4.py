def synchronize_databases(legacy_list, modern_set, blacklist):
    legacy_ids = set()

    for record in legacy_list:
        record_id = record[0]
        email = record[1]

        if email not in blacklist:
            legacy_ids.add(record_id)

    lost_set = set()
    for record_id in legacy_ids:
        if record_id not in modern_set:
            lost_set.add(record_id)

    ghost_set = set()
    for record_id in modern_set:
        if record_id not in legacy_ids:
            ghost_set.add(record_id)

    return lost_set, ghost_set

Legacy = [(101, "ali@mail.com"), (102, "sara@mail.com")]
Modern =  {101, 105}
Blacklist = {"sara@mail.com"}

print (synchronize_databases(Legacy,Modern,Blacklist))