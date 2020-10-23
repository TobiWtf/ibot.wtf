## Written with love by tobi <3 

from app.main import run
import multiprocessing, platform


def BuildKwargs(**kwargs):
    return kwargs


SSLPath: str = r"SslConfiguration/ibot.wtf"

if __name__ == "__main__":
    if platform.system().lower() == "windows":
        multiprocessing.freeze_support()

    multiprocessing.Process(
        target=run, kwargs=BuildKwargs(
            ssl_certfile=SSLPath + "/cert.pem",
            ssl_keyfile=SSLPath + "/privkey.pem",
            host="0.0.0.0",
            port=443,
        )
    ).start()
    multiprocessing.Process(
        target=run, kwargs=BuildKwargs(
            host="0.0.0.0",
            port=80,
        )
    ).start()
