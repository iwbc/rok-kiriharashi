# This Python file uses the following encoding: utf-8

import os
import sys
from android_auto_play_opencv import AapoManager

INCLUDES_DIR_PATH = os.path.join(os.path.dirname(__file__), "includes", "")
ADB_DIR_PATH = os.path.join(os.path.dirname(__file__), "bin", "")

# 斥候キャンプタップ位置
SCOUT_CAMP_TAP_POS = (800, 450)

aapo = None


def main():
    global aapo

    aapo = AapoManager(ADB_DIR_PATH)
    devices = aapo.adbl.devices

    for i, device in enumerate(devices):
        if device == "":
            continue
        print(f"{i + 1}: {device}")

    try:
        deviceNo = int(input("\n操作するエミュレーターの番号を入力してください: "))
        device = devices[deviceNo - 1]
        aapo.adbl.setdevice(device)
    except:
        print("無効な入力値です。処理を中止します。")
        sys.exit(1)

    print(f"\n===== 探索開始（CTRL+Cで終了） =====\n")

    kiriharashi()


def kiriharashi():
    while True:
        print(f"\n===== 派遣可能になるまで待機 =====\n")
        try:
            checkImg(
                os.path.join(INCLUDES_DIR_PATH, "scout_explore.png"), infinite=True
            )
            aapo.sleep(3)
        except AppRestarted:
            openScoutCamp()
            continue

        print(f"\n===== 霧選択 =====\n")
        try:
            checkImg(os.path.join(INCLUDES_DIR_PATH, "scout_explore.png"))
        except TimeoutError:
            backHome()
            continue
        except AppRestarted:
            openScoutCamp()
            continue
        aapo.sleep(1)

        print(f"\n===== 斥候派遣 =====\n")
        try:
            checkImg(os.path.join(INCLUDES_DIR_PATH, "scout_send.png"))
        except TimeoutError:
            backHome()
            continue
        except AppRestarted:
            openScoutCamp()
            continue

        aapo.sleep(1)
        backHome()


def backHome():
    print(f"\n===== 都市に戻る =====\n")
    checkImg(os.path.join(INCLUDES_DIR_PATH, "home.png"))
    aapo.sleep(5)
    openScoutCamp()


def openScoutCamp():
    print(f"\n===== 斥候キャンプ =====\n")
    aapo.touchPos(SCOUT_CAMP_TAP_POS[0], SCOUT_CAMP_TAP_POS[1])
    aapo.sleep(1)
    checkImg(os.path.join(INCLUDES_DIR_PATH, "scout.png"))
    aapo.sleep(1)


def checkImg(
    img_path: str,
    tap: bool = True,
    infinite: bool = False,
):
    timer = 0
    while True:
        aapo.screencap()
        result, x, y = aapo.chkImg2(img_path)

        if result:
            if tap:
                aapo.sleep(1)
                aapo.touchPos(x, y)
            break
        elif timer >= 9:
            icon_bs = os.path.join(INCLUDES_DIR_PATH, "icon_bs.png")
            icon_nox = os.path.join(INCLUDES_DIR_PATH, "icon_nox.png")
            if aapo.touchImg(icon_bs):
                aapo.sleep(60)
                raise AppRestarted
            elif aapo.touchImg(icon_nox):
                aapo.sleep(60)
                raise AppRestarted
            elif not infinite:
                raise TimeoutError
        else:
            timer += 1
            aapo.sleep(1)


class AppRestarted(Exception):
    pass


if __name__ == "__main__":
    main()
