image bg natsuki_house = "images/bg/house.jpg"
image bg natsuki_bedroom = "mod_assets/natsuki_bedroom.png"
image bg bathroom = "mod_assets/bathroom.png"

init 10 python:
    build.archive("mod_assets", "all")
    build.classify("game/mod_assets/**", "mod_assets")
    config.label_overrides["start"] = "start_mod"
    config.label_overrides["splashscreen"] = "splashscreen_mod"
    splash_message_default = "This game is an unofficial fan work, unaffiliated with Team Salvato."

init 10:
    define config.name = "F.T.S."
    define gui.show_name = False
    define build.name = "DDLC_FTS"
    define config.save_directory = "DDLC-FTS"
    screen navigation():
        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            yalign 0.8
            spacing gui.navigation_spacing
            if not persistent.autoload or not main_menu:
                if main_menu:
                    textbutton _("New game") action Start()
                else:
                    textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
                    textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]
                textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]
                if _in_replay:
                    textbutton _("End Replay") action EndReplay(confirm=True)
                elif not main_menu:
                    textbutton _("Main Menu") action MainMenu()
                textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
                if renpy.variant("pc"):
                    textbutton _("Help") action Help("README.html")
                    textbutton _("Quit") action Quit(confirm=not main_menu)
            else:
                timer 1.75 action Start("autoload_yurikill")

label start_mod:
    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = True
    call story
    call endgame
    return

label splashscreen_mod:
    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and not persistent.do_not_delete:
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting saves...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass
        python:
            if not firstrun:
                with open(config.basedir + "/game/firstrun", "w") as f:
                    f.write("1")
            filepath = renpy.file("firstrun").name
            open(filepath, "a").close()
    default persistent.first_run = False
    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos with Dissolve(1.0)
        pause 1.0
        "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
        menu:
            "By playing [config.name] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."
            "I agree.":
                pass
        scene tos2 with Dissolve(1.5)
        pause 1.0
        scene white with Dissolve(1.5)
        $ persistent.first_run = True
    $ basedir = config.basedir.replace('\\', '/')
    if persistent.autoload and not _restart:
        jump autoload
    $ config.allow_skipping = False
    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label story_transition_school:
    scene bg natsuki_house with wipeleft_scene
    scene bg corridor with wipeleft_scene
    scene bg class_day with wipeleft_scene
    play music t2
    return

label story_transition_club:
    stop music fadeout 2.0
    scene bg corridor with wipeleft_scene
    scene bg club_day with wipeleft_scene
    play music t3
    return

label story_transition_home:
    stop music fadeout 2.0
    scene bg corridor with wipeleft_scene
    scene bg natsuki_house with wipeleft_scene
    play music t8
    return

label story_transition_nextday:
    stop music fadeout 2.0
    scene bg natsuki_bedroom with wipeleft_scene
    return

label story_transition_glitch:
    stop music
    show screen tear(40, 0.1, 0.1, 0, 80)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    $ _history_list.pop()
    return
