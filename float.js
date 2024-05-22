const SteamUser = require('steam-user');
const GlobalOffensive = require('globaloffensive');
const readline = require('readline'); // Thêm thư viện readline

const client = new SteamUser();
const csgo = new GlobalOffensive(client);

const logOnOptions = {
  accountName: 'thongplayass',
  password: 'Godlike313',
  twoFactorCode: '' // Bỏ trống, sẽ nhập khi được yêu cầu
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

client.logOn(logOnOptions);

client.on('loggedOn', () => {
  console.log('Logged into Steam');
  client.setPersona(SteamUser.EPersonaState.Online);
  client.gamesPlayed([730]);
});

client.on('error', (err) => {
  console.error('An error occurred:', err);
});

client.on('steamGuard', (domain, callback) => {
  console.log('Steam Guard code needed');
  rl.question('Please enter Steam Guard code: ', (code) => {
    callback(code);
    rl.close();
  });
});

csgo.on('connectedToGC', () => {
  console.log('Connected to CS:GO GC');

  // Yêu cầu giá trị float từ inspect link
  const inspectLink = 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198282050545A37461810854D5496256354796995687';
  console.log('Inspect link:', inspectLink);

  // Phân tích chuỗi inspect link để lấy các giá trị cần thiết
  const inspectParams = inspectLink.match(/S(\d+)A(\d+)D(\d+)/);
  if (inspectParams && inspectParams.length === 4) {
    const steamId = inspectParams[1];
    const assetId = inspectParams[2];
    const dParam = inspectParams[3];

    console.log('Parsed steamId:', steamId);
    console.log('Parsed assetId:', assetId);
    console.log('Parsed dParam:', dParam);

    csgo.inspectItem(steamId, assetId, dParam, (err, item) => {
      if (err) {
        return console.log('Error inspecting item:', err);
      }

      console.log('Item details:', item);
      if (item && item.paintwear !== undefined) {
        console.log('Float value:', item.paintwear);
      } else {
        console.log('Failed to retrieve float value');
      }
    });
  } else {
    console.log('Invalid inspect link format');
  }
});

csgo.on('disconnectedFromGC', (reason) => {
  console.log('Disconnected from GC:', reason);
});

csgo.on('error', (err) => {
  console.error('An error occurred in CS:GO module:', err);
});
