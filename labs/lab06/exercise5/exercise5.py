def audit_zero_trust(baseline_set, current_log_list):

   current_logs = set()

   for log in current_log_list:
        current_logs.add(log)

   authorized = set()
   alerts = set()
    
   for entry in current_logs:
      if entry in baseline_set:
         authorized.add(entry)
      else : 
         alerts.add(entry)

   inactive = set()
   for entry in baseline_set:
      if entry not in current_logs:
            inactive.add(entry)

   return authorized, alerts, inactive
