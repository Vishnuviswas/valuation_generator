const { app, BrowserWindow } = require("electron");
const { spawn } = require("child_process");
const http = require("http");
const path = require("path");

let mainWindow;

function waitForServer(url, callback) {
    const check = () => {
        http.get(url, () => callback()).on("error", () => {
            setTimeout(check, 1000);
        });
    };
    check();
}

app.whenReady().then(() => {

    // ✅ Absolute paths
    const pythonPath = "E:\\vishnu viswas\\ai_valuation\\ai_valuation\\Scripts\\python.exe";
    const appPath = "E:\\vishnu viswas\\ai_valuation\\src\\ui\\streamlit_app.py";

    const streamlit = spawn(
        pythonPath,
        [
            "-m",
            "streamlit",
            "run",
            appPath,
            "--server.port=8501",
            "--server.headless=true"
        ],
        { shell: false }
    );

    streamlit.stdout.on("data", (data) => {
        console.log(data.toString());
    });

    streamlit.stderr.on("data", (data) => {
        console.log(data.toString());
    });

    waitForServer("http://localhost:8501", () => {
        mainWindow = new BrowserWindow({
            width: 1200,
            height: 800,
        });

        mainWindow.loadURL("http://localhost:8501");
    });
});