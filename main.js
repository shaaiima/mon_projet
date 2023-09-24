const { app, BrowserWindow } = require('electron');
const path = require('path');
const url = require('url');

let mainWindow;

app.on('ready', () => {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });

  mainWindow.loadFile('index.html');

  // Charger une page différente lorsque le bouton est cliqué
  const loadPage = (pageName) => {
    mainWindow.loadFile(`${pageName}.html`);
  };

  // Créer un lien global vers la fonction loadPage pour qu'elle puisse être appelée depuis le rendu
  mainWindow.webContents.on('did-finish-load', () => {
    mainWindow.webContents.executeJavaScript(`window.loadPage = ${loadPage.toString()}`);
  });
});

