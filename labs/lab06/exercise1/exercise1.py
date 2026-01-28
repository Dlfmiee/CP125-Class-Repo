def get_legit_power_users(log_data, bot_ids, threshold):

    user_actions = {}

    for entry in log_data:
        timestamp = entry[0]
        user_id = entry[1]
        action_type = entry[2]
        
        if user_id in bot_ids:
            continue
        
        if user_id not in user_actions:
            user_actions[user_id] = []
        
        if action_type not in user_actions[user_id]:
            user_actions[user_id].append(action_type)
    
    power_users = []
    for user_id in user_actions:
        if len(user_actions[user_id]) > threshold:
            power_users.append(user_id)
    
    power_users.sort()
    return power_users
