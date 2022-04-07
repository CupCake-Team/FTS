label story_act1_begin(fridge='found only beer and dried fish', eatable=False, study='improve your grades'):
    call story_transition_nextday
    menu:
        "{i}You get up from bed.{/i}"
        "Get some breakfast.":
            pass
    hide bg natsuki_bedroom with wipeleft_scene
    "{i}You open the fridge and [fridge].{/i}"
    if eatable:
        menu:
            "{i}You take it quickly.{/i}"
            "Get ready for school.":
                  pass
    else:
        menu:
             "{i}You wouldn't eat any of these.{/i}"
             "Get ready for school.":
                  pass
    scene bg natsuki_bedroom with wipeleft_scene
    menu:
        "{i}You packed up a bag and changed to school uniform.{/i}"
        "Go to school.":
            pass
    call story_transition_school
    menu:
        "{i}You got to the class.{/i}"
        "Study.":
            pass
    menu:
        "{i}You're studying.{/i}"
        "Study harder.":
            "{i}You study harder and [study].{/i}"
    menu:
        "{i}Classes are over.{/i}"
        "Go to club.":
            pass
    call story_transition_club
    menu:
        "{i}You got to the club.{/i}"
        "Do some club activities.":
            pass
    return

label story_act2_begin(fridge='found only beer and dried fish', eatable=False, study='that wouldn\'t improve your grades'):
    call story_transition_nextday
    menu:
        "{i}You get up from bed.{/i}"
        "Try to get some breakfast.":
            pass
    hide bg natsuki_bedroom with wipeleft_scene
    "{i}You open the fridge and [fridge].{/i}"
    if eatable:
        menu:
            "{i}You take it quickly.{/i}"
            "Try to get ready for school.":
                  pass
    else:
        menu:
             "{i}You wouldn't eat any of these.{/i}"
             "Try to get ready for school.":
                  pass
    scene bg natsuki_bedroom with wipeleft_scene
    menu:
        "{i}You packed up a bag and changed to school uniform.{/i}"
        "Try to get to school.":
            pass
    call story_transition_school
    menu:
        "{i}You got to the class.{/i}"
        "Try to study.":
            pass
    menu:
        "{i}You're studying.{/i}"
        "Try to study harder.":
            "{i}You tried study harder but [study].{/i}"
    menu:
        "{i}Classes are over.{/i}"
        "Try to go to club.":
            pass
    call story_transition_club
    menu:
        "{i}You got to the club.{/i}"
        "Try to do some club activities.":
            pass
    return

label story_act1_end (homework=True, poem=True):
    call story_transition_home
    menu:
        "{i}You got to your home.{/i}"
        "Enter the house.":
            pass
    scene bg natsuki_bedroom with wipeleft_scene
    menu:
        "{i}You entered the house.{/i}"
        "Do homework." if poem:
            if homework:
                menu:
                    "{i}You've done the homework.{/i}"
                    "Write a poem.":
                        pass
            menu:
                "{i}You wrote a poem for the club, {w=1.0}when suddenly your father calls you for dinner.{/i}"
                "Get some dinner.":
                    pass
        "Get some dinner." if not poem:
            pass
    hide bg natsuki_bedroom with wipeleft_scene
    menu:
        "{i}You went to the kitchen and had a nice dinner.{/i}"
        "Take a shower.":
            pass
    scene bg bathroom with wipeleft_scene
    menu:
        "{i}You took a shower.{/i}"
        "Go to sleep.":
            pass
    hide bg bathroom with wipeleft_scene
    menu:
        "{i}You went back to the bedroom and went to sleep.{/i}"
        "Get up from bed.":
            pass
    return

label story_act2_end (homework=True, poem=True):
    call story_transition_home
    menu:
        "{i}You got to your home.{/i}"
        "Try to enter the house.":
            pass
    scene bg natsuki_bedroom with wipeleft_scene
    menu:
        "{i}You entered the house.{/i}"
        "Try to do homework." if poem:
            if homework:
                menu:
                    "{i}You've done the homework.{/i}"
                    "Write a poem.":
                        pass
            "{i}You wrote a poem for the club, {w=1.0}when suddenly your father calls you for dinner...{/i}"
            menu:
                "{i}You don't like where this is going.{/i}"
                "Try to dinner.":
                    pass
        "Try to dinner." if not poem:
            pass
    hide bg natsuki_bedroom with wipeleft_scene
    "{i}You went to the kitchen.{/i}"
    "{i}There was quite a bit of food for dinner.{/i}"
    "{i}Your drunk father yelled at you and hit you.{w=3.0}{nw}{/i}"
    menu:
        "{i}You left the kitchen in tears.{/i}"
        "Try to take a shower.":
            pass
    scene bg bathroom with wipeleft_scene
    menu:
        "{i}You took a shower.{/i}"
        "Try to sleep.":
            pass
    hide bg bathroom with wipeleft_scene
    menu:
        "{i}You went back to the bedroom and went to sleep.{/i}"
        "Try to get up from bed.":
            pass
    return

label story:
    stop music fadeout 2.0
    scene black with dissolve_scene_full
    call story_act1_begin
    menu:
        "{i}After greeting everyone, you were about to start reading manga, {w=1.0}when suddenly a boy is brought into the club.{/i}"
        "Meet the newcomer.":
            "{i}You're getting to know that guy.{/i}"
    menu:
        "{i}It's time for a surprise for the club.{/i}"
        "Get the Surprise.":
            pass
    menu:
        "{i}You secretly took out the tray with the cupcakes you had made under it.{/i}"
        "Reveal the cupcakes.":
            pass
    menu:
        "{i}After you lifted the foil off the tray to reveal cupcakes, everyone graps one.{/i}"
        "Wait until the end of the club meeting.":
            "{i}After enjoying your cupcakes, and enjoying a tea from your friend, you heard the assignment from club president for tomorrow.{/i}"
    menu:
        "{i}And thus the meeting was completed.{/i}"
        "Go home.":
            pass
    call story_act1_end
    call story_act1_begin pass (fridge='found a sandwich', eatable=True)
    "{i}You exchange poems with the rest of the club.{/i}"
    menu:
        "{i}You are most impressed with the guy's poem.{/i}"
        "Read some manga.":
            pass
    scene bg closet with wipeleft_scene
    menu:
        "{i}You decide to read manga, when suddenly a guy is interested in your hobby.{/i}"
        "Discuss about manga with a guy.":
            pass
    menu:
        "{i}You discussed the manga with a guy and were able to form a kind of friendship with him.{/i}"
        "Read manga with guy.":
            "{i}You were reading manga with a guy, {w=1.0}when suddenly the club meeting was over.{/i}"
    menu:
        "{i}You decide to give this manga volume to guy to finish reading at home.{/i}"
        "Go home.":
            pass
    call story_act1_end
    call story_act1_begin pass (fridge='found that the amount of beer and snacks with it has decreased significantly..')
    "{i}You exchange poems with the rest of the club.{/i}"
    menu:
        "{i}A guy is showing some progress in poetry.{/i}"
        "Read some manga.":
            pass
    scene bg closet with wipeleft_scene
    menu:
        "{i}You went to the closet to read manga when you suddenly discovered that the club leader had moved your manga to the top shelf.{/i}"
        "Figure out a way to get manga.":
            "{i}A guy came up to you in order to understand what happened.{/i}"
    "{i}After giving him a few quips in return, you figured out how to get the manga and hopped on the office chair.{/i}"
    menu:
        "{i}You wheeled it to the closet.{/i}"
        "Try to get the manga.":
            "{i}You stood up on the office chair, while a guy held it up so you wouldn't fall over.{/i}"
    "{i}The attempt to get one of the manga boxes failed due to a skirt incident.{\i}"
    menu:
        "{i}You ended up falling down with the manga.{/i}"
        "Realize what happened.":
            "{i}Turns out you fell right on a guy.{/i}"
    "{i}When you saw the crumpled manga around you, you began to unintentionally cry over the sad memories.{/i}"
    menu:
        "{i}After calming down, you and a guy put the manga back.{/i}"
        "Wait until the end of the club meeting.":
            pass
    menu:
        "{i}And thus the meeting was completed.{/i}"
        "Go home.":
            pass
    call story_act1_end
    call story_act1_begin pass (fridge='find a small chocolate bar next to a restocked beer', eatable=True, study='get on the school honor board')
    "{i}You exchange poems with the rest of the club.{/i}"
    menu:
        "{i}A guy wrote a good poem.{/i}"
        "Read some manga.":
            pass
    menu:
        "{i}You were about to begin reading manga, when suddenly the club leader made an announcement regarding the preparations for the school festival that brought you in too."
        "Join the discussion.":
            "{i}After the discussion was concluded, it was clear who was going to do what.{/i}"
    menu:
        "{i}Thanks to your eloquence, a guy decided to help you with baking a cupcakes.{/i}"
        "Wait until the end of the club meeting.":
            pass
    menu:
        "{i}And thus the meeting was completed.{/i}"
        "Go home.":
            pass
    call story_act1_end pass (homework=False)
    call story_transition_nextday
    menu:
        "{i}You get up from bed.{/i}"
        "Get some breakfast.":
            pass
    hide bg natsuki_bedroom with wipeleft_scene
    "{i}You opened the fridge and found a can of soda.{/i}"
    menu:
        "{i}You drank it off quickly.{/i}"
        "Prepare ingredients for cupcakes.":
            pass
    menu:
        "{i}You have prepared a large bag of ingredients.{/i}"
        "Go to guy's house.":
            pass
    scene bg natsuki_house with wipeleft_scene
    scene bg residential_day with wipeleft_scene
    scene bg house with wipeleft_scene
    "{i}You have reached a guy's house.{/i}"
    menu:
        "{i}A guy himself was waiting for you outside.{/i}"
        "Enter the house.":
            pass
    scene bg kitchen with wipeleft_scene
    menu:
        "{i}You entered the house.{/i}"
        "Begin cupcake baking.":
            pass
    "{i}Except a couple of awkward moments, the cupcakes bake-off with the guy was successful.{/i}"
    menu:
        "{i}You, as well as he, were satisfied with the work done.{/i}"
        "Go home.":
            pass
    call story_act1_end pass (poem=False)
    call story_transition_nextday
    "{i}You get up from be{/i}{nw}"
    call story_transition_glitch
    scene black
    pause 2
    call story_act2_begin
    "{i}After greeting everyone, you were about to start reading manga, when suddenly a boy is brought into the club.{/i}"
    menu:
        "{i}This situation seems familiar.{/i}"
        "Try to meet the newcomer.":
            pass
    menu:
        "{i}You're getting to know that guy. It's time for a surprise for the club.{/i}"
        "Try to get the Surprise.":
            pass
    menu:
        "{i}You secretly took out the tray with the cupcakes you had made under it.{/i}"
        "Reveal the cupcakes.":
            pass
    menu:
        "{i}After you lifted the foil off the tray to reveal cupcakes, everyone graps one.{/i}"
        "Try to wait until the end of the club meeting.":
            pass
    "{i}After enjoying your cupcakes, and enjoying a tea from your friend, you heard the assignment from club president for tomorrow.{/i}"
    menu:
        "{i}And thus the meeting was completed.{/i}"
        "Try to go home.":
            pass
    call story_act2_end
