"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""
₪ **Find out all the Bot's commands and how they work by clicking on the » ◍⌊Commands⌉ button!**
₪ **To know how to use this bot, please click on the » ◍⌊Guide⌉ button!**""",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⩡ Add Robot",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("▣⌊Donate⌉", url=f"https://t.me/{OWNER_USERNAME}")],
                [
                    InlineKeyboardButton("◍⌊Commands⌉", callback_data="command_list"),
                    InlineKeyboardButton("◍⌊Quick Guide⌉", callback_data="user_guide"),
                    InlineKeyboardButton("◍⌊🇮🇷 Guide⌉", callback_data="quick_use"),
                ],
                [
                    InlineKeyboardButton(
                        "₪⌊Sup-Group⌉", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "₪⌊Channel⌉", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("راهنــمای پـارسی")
    await query.edit_message_text(
        f"""ℹ️ راهنمای سریع فارسی استفاده از ربات!
₪ افزودن ربات
⨞ **برای استفاده از ربات ابتدا توسط دکمه پایین ، اونو تو گروهت اضافه و سپس مدیر کن . برای این کار کار قابلیت های حداقلی زیر رو بهش بده
**
✓ delete messages - حذف پیام
✓ invite users - دعوت کاربران
✓ manage video chats - مدیریت ویدیوچت
✓ pin messages - سنجاق پیام ها
※ در صورت انجام ندادن این مرحله قابلیت استفاده از ربات برای گروه شما وجود نخواهد داشت
———
₪ **دستورات مهم استریم | صرفاادمین گروه**
⨞ بعد از اضافه کردن ادمین جدید برای شناسایی شدنش توسط ربات یک بار از دستور `/reload` استفاده کُن
—→ `/play` - **برای پخش آهنگ توی ویدیوچت از این دستور استفاده کن**
           - تایپ دستور و بلافاصله اسم آهنگ(هر زبانی باشد فرق نمی کند)
           - ریپلای `/play` یا `.play` روی فایل صوتی
—→ `/vplay` - **برای پخش ویدیو توی ویدیوچت از این دستور استفاده کن**
            - تایپ دستور و بلافاصله اسم ویدیو
            - ریپلای `/vplay` یا `.vplay` روی فایل ویدیویی
₪در صورت وجود اشکال در استفاده و نصب به [گروه پشتیبانی](https://t.me/{GROUP_SUPPORT}) مراجعه کن.
₪ **بقیه دستورات کاربردی در لینک کانال موجود در INFO بـات**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضافه کردن ربات",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],[
                    InlineKeyboardButton("⌂Home", callback_data="home_start")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""❓ To know how to use this Bot, read the Guide below !
1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{me_user.username} to your group or type /userbotjoin to invite her, unfortunately the userbot will joined by itself when you type `/play (song name)` or `/vplay (song name)`.
4.) Turn on/Start the video chat first before start to play video/music.

    END, EVERYTHING HAS BEEN SETUP!

💡 If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⌂Home", callback_data="home_start")]]
        ),
    )

@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **[{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !** , Check out the menu below to read list of available Commands !
**Use Commands With (`!` `/` `.`) Handler**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⩥Admins Commands", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("⩥Users Commands", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("⁕Sudo Commands", callback_data="sudo_command"),
                    InlineKeyboardButton("⁕Owner Commands", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("⌂Home", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""⪢ Command list for all user.
» /play (song name/link) ⇒ **play music on video chat**
» /vplay (video name/link) ⇒ **play video on video chat**
» /playlist ⇒ **see the current playing song**
» /lyric (query) ⇒ **scrap the song lyric**
» /video (query) ⇒ **download video from youtube**
» /song (query) ⇒ **ownload song from youtube**
» /search (query) ⇒ **search a youtube video link**
» /ping ⇒ **show the bot ping status**
» /uptime ⇒ **show the bot uptime status**
» /alive ⇒ **show the bot alive info** (in Group only)
⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⪡Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""⪢ Command list for group admin.
» /pause ⇒ **pause the current track being played**
» /resume ⇒ **play the previously paused track**
» /skip ⇒ **goes to the next track**
» /stop ⇒ **stop playback of the track and clears the queue**
» /vmute ⇒ **mute the streamer userbot on group call**
» /vunmute ⇒ **unmute the streamer userbot on group call**
» /volume `1-200` ⇒ **adjust the volume of music (userbot must be admin)**
» /reload ⇒ **reload bot and refresh the admin data**
» /userbotjoin ⇒ **invite the userbot to join group**
» /userbotleave ⇒ **order userbot to leave from group**
» /startvc ⇒ **start/restart the group call**
» /stopvc ⇒ **stop/discard the group call**
⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⪡Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in SUDO_USERS:
        await query.answer("⨉ You don't have permissions to click this button", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""✏️ Command list for sudo user.
» /stats ⇒ **get the bot current statistic**
» /calls ⇒ **show you the list of all active group call in database**
» /block (`chat_id`) ⇒ **use this to blacklist any group from using your bot**
» /unblock (`chat_id`) ⇒ **use this to whitelist any group from using your bot**
» /blocklist ⇒ **show you the list of all blacklisted chat**
» /speedtest ⇒ **run the bot server speedtest**
» /sysinfo ⇒ **show the system information**
» /logs ⇒ **generate the current bot logs**
» /eval ⇒ **execute any code (`developer stuff`)**
» /sh ⇒ **run any command (`developer stuff`)**
⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⪡Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in OWNER_ID:
        await query.answer("⨉ You don't have permissions to click this button", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f""" Command list for bot owner.
» /gban (`username` or `user_id`) ⇒ for global banned people, can be used only in group
» /ungban (`username` or `user_id`) ⇒ for un-global banned people, can be used only in group
» /update ⇒ update your bot to latest version
» /restart ⇒ restart your bot directly
» /leaveall ⇒ order userbot to leave from all group
» /leavebot (`chat id`) ⇒ order bot to leave from the group you specify
» /broadcast (`message`) ⇒ send a broadcast message to all groups in bot database
» /broadcast_pin (`message`) ⇒ send a broadcast message to all groups in bot database with the chat pin
⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⪡Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
