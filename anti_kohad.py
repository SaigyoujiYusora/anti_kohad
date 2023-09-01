import itertools
import os
import random
import hoshino
from hoshino import Service, priv, R
from hoshino.config import RES_DIR
from hoshino.typing import CQEvent

# sv = Service('anti-KohaD', enable_on_default=False,manage_priv=priv.ADMIN)
sv = Service(
    name='anti-KohaD',  # 功能名
    use_priv=priv.NORMAL,  # 使用权限
    manage_priv=priv.ADMIN,  # 管理权限
    visible=True,  # 可见性
    enable_on_default=True,  # 默认启用
    bundle='娱乐',  # 分组归类
    # help_ = sv_help #帮助说明
)
imgpath = os.path.join(os.path.expanduser(RES_DIR), 'img', 'kohad')
pandoraimgpath = os.path.join(os.path.expanduser(RES_DIR), 'img', 'kohad', 'maimai')

QRCODE_RECALL_MSG_TIME = 45

kohad = '''
kohad KohaD KOHAD 弱虫 麒麟 秒针 39 100块 一百块 潘 潘多拉 白潘 8em 8EM 8-em 紅蓮華 MIRACLE RUSH Pretender 红莲华 loser LOSER usa
USA u.s.a. U.S.A. 你不知道的故事 君の知らない物語 物語 物语 咬住秒针 秒針を噛む ArtyParty 
'''


@sv.on_keyword(kohad)
# @sv.on_rex(r'(嘉[\.\s]*(然|人))|(嘉[\.\s]*心[\.\s]*糖)')
async def anti_kohad(bot, ev: CQEvent):
    kohad_img = "shanle.jpg"
    ruochong_img = "ruochong.jpg"
    S100_img = "100kuai.jpg"
    pandora_img = random.choice(os.listdir(pandoraimgpath))
    eight_em_img = "8em.jpg"

    ranum = random.random()

    if '39music' in ev.message.extract_plain_text():
        pass
    elif '弱虫' in ev.message.extract_plain_text():
        try:
            sentimg = R.img(f'kohad/{ruochong_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取弱虫梗图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    elif ('一百块' or '100块') in ev.message.extract_plain_text():
        try:
            sentimg = R.img(f'kohad/{S100_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取一百块梗图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    elif ('潘' or '潘多拉' or '白潘') in ev.message.extract_plain_text():
        try:
            sentimg = R.img(f'kohad/pan/{pandora_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取潘梗图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    elif ('8em' or '8EM' or '8-em') in ev.message.extract_plain_text():
        try:
            sentimg = R.img(f'kohad/{eight_em_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取8em梗图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    else:
        try:
            sentimg = R.img(f'kohad/{kohad_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取KohaD弔图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    hoshino.logger.info(f'anti_kohad随机数为{ranum}')


# playMaiMai= '''
# 打舞萌打的 玩舞萌dx玩的 打mai打的 打舞萌dx打的
# '''.split()
playMaiMai = list(map(''.join, itertools.product(
    ('', '鉴定为'),
    ('打', '玩'),
    ('舞萌', 'mai'),
    ('', 'mai'),
    ('', 'dx'),
    ('玩的', '打的'),
)))


@sv.on_keyword(*playMaiMai)
async def play_maimai(bot, ev: CQEvent):
    imgpath = os.path.join(os.path.expanduser(RES_DIR), 'img', 'kohad', 'maimai')
    playMaiMaipic = random.choice(os.listdir(imgpath))
    try:
        playMaiMaipic = R.img(f'kohad/maimai/{playMaiMaipic}').cqcode
    except Exception as e:
        hoshino.logger.error(f'读取打舞萌梗图时发生错误{type(e)}')
    await bot.send(ev, playMaiMaipic)


yuyuzheng = list(map(''.join, itertools.product(
    ('我有', ''),
    ('玉玉', '郁郁', '抑郁'),
    ('症', '了'),
)))


@sv.on_keyword(*yuyuzheng)
async def yuyuzheng(bot, ev: CQEvent):
    imgpath = os.path.join(os.path.expanduser(RES_DIR), 'img', 'kohad', 'yuyuz')
    yuyuzhengpic = random.choice(os.listdir(imgpath))
    randomnum = random.random()

    if randomnum < 0.05:
        try:
            yuyuzhengpic = R.img(f'kohad/yuyuz/{yuyuzhengpic}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取玉玉梗图时发生错误{type(e)}')
        await bot.send(ev, yuyuzhengpic)
    hoshino.logger.info(f'玉玉症随机数为{randomnum}')

godlist = list(map(''.join, itertools.product(
    # ('', '舞', '星', '真', '雪'),
    # ('', '神', '将', '极', '急', '寄'),
    ('幻空', '薄荷', '纸巾', 'fww', 's', 'S', 'alan', 'Alan', 'ALAN', 'kira', 'Kira', 'kpc', 'KPC', '千叶'),
    ('', '舞', '星', '真', '雪'),
    ('神', '叠', '爹', '大佬', 'dalao', '大神', '佬', '将', '极', '急', '寄'),
    ('', '啊', '水平')
)))


@sv.on_keyword(*godlist)
async def anti_mairuo(bot, ev: CQEvent):
    # godpic = "dalao.jpg"
    godpic = "jiushia.PNG"
    randomnum = random.random()

    if randomnum < 0.1:
        try:
            godpic = R.img(f'kohad/{godpic}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取大神梗图时发生错误{type(e)}')
        await bot.send(ev, godpic)
    hoshino.logger.info(f'大神麦若随机数为{randomnum}')

qrcode = list(map(''.join, itertools.product(
    ('牛', '投币', '舞萌'),
    ('', '二维'),
    ('码', '马'),
)))


@sv.on_keyword(*qrcode)
async def qrcode(bot, ev: CQEvent):
    qrcodepic = "qrcode.jpg"
    try:
        qrcodepic = R.img(f'kohad/{qrcodepic}').cqcode
    except Exception as e:
        hoshino.logger.error(f'读取二维码图片时发生错误{type(e)}')
    await bot.send(ev, qrcodepic)

