import requests
import json
import re

def get_steam_inventory():
    url = "https://steamcommunity.com/inventory/76561198282050545/730/2?l=english&count=5000"
    headers = {"Content-Type": "application/json"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        inventory_data = response.json()
        descriptions = inventory_data.get("descriptions", [])
        assets = inventory_data.get("assets", [])
        
        # Tạo dictionary để tra cứu nhanh asset
        asset_dict = {asset['assetid']: asset for asset in assets}

        items = []

        for description in descriptions:
            classid = description['classid']
            instanceid = description.get('instanceid', '0')  # Có thể không có instanceid
            market_hash_name = description.get('market_hash_name', 'N/A')
            marketable = description.get('marketable', 0)
            
            # Tìm asset liên quan đến description này
            for assetid, asset in asset_dict.items():
                if asset['classid'] == classid and asset.get('instanceid', '0') == instanceid:
                    owner_steamid = '76561198282050545'  # SteamID của người dùng
                    assetid = asset['assetid']

                    # Lấy link gốc từ description actions
                    original_link = ''
                    if 'actions' in description:
                        original_link = description['actions'][0]['link']
                        # Sử dụng regex để lấy giá trị D từ original_link
                        match = re.search(r'D(\d+)', original_link)
                        if match:
                            correct_d_value = match.group(1)
                        else:
                            correct_d_value = '0'
                    else:
                        correct_d_value = '0'
                    
                    inspect_link = f"steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S{owner_steamid}A{assetid}D{correct_d_value}"

                    items.append({
                        "market_name": market_hash_name,
                        "marketable": marketable,
                        "link": inspect_link
                    })
                    break

        # Save all item data to a JSON file
        with open('full_inventory.json', 'w') as f:
            json.dump(items, f, indent=4)

        return "Full inventory saved to 'full_inventory.json'"
    else:
        return "Failed to retrieve inventory"

# Gọi hàm để lấy inventory và in kết quả
inventory = get_steam_inventory()
print(inventory)
