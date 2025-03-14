# Define characters
define mc = Character("[name]", color="#5f9ea0") # Protagonist 
define principal = Character("Principal Yamada", color="#8b4513")
define shion = Character("Shion Mizuki", color="#9370db")
define thoughts = Character(None, italic=True) # For inner monologues - adds italics to differentiate them

# Screen settings for 1080p with 832x1216 sprites
init:
    # Set the game to 1080p resolution
    $ config.screen_width = 1920
    $ config.screen_height = 1080
    
    # Define proper scaling for character sprites (832x1216)
    $ center_sprite_offset = 0.0    # Default center position
    $ left_sprite_offset = -0.25    # 25% from center toward left
    $ right_sprite_offset = 0.25    # 25% from center toward right
    
    # Custom transforms for character positioning with appropriate scaling for 832x1216 sprites
    transform center_sprite:
        xalign 0.5
        yalign 1.0
        zoom 0.7  # Adjusted scaling for 832x1216 sprites
        
    transform left_sprite:
        xalign 0.25
        yalign 1.0
        zoom 0.7
        
    transform right_sprite:
        xalign 0.75
        yalign 1.0
        zoom 0.7

# Background images (1920x1080 resolution)
# These are full-screen background images, not character sprites
image bg school_exterior = im.Scale("backgrounds/bg_school_exterior.jpg", 1920, 1080)
image bg school_hallway = im.Scale("backgrounds/bg_school_hallway.jpg", 1920, 1080)
image bg music_room = im.Scale("backgrounds/bg_music_room.jpg", 1920, 1080)
image bg music_room_door = im.Scale("backgrounds/bg_music_room_door.jpg", 1920, 1080) # View through door window
image bg art_room = im.Scale("backgrounds/bg_art_room.jpg", 1920, 1080)
image bg art_room_door = im.Scale("backgrounds/bg_art_room_door.jpg", 1920, 1080)

# Activity background images (showing piano/painting activities)
image bg shion_piano = im.Scale("backgrounds/shion_piano.jpg", 1920, 1080)      # Shion at piano (background)
image bg shion_piano_side = im.Scale("backgrounds/shion_piano_side.jpg", 1920, 1080) # Side view of piano playing
image bg shion_painting = im.Scale("backgrounds/shion_painting.jpg", 1920, 1080) # Shion painting (background)

# Character sprites (832x1216 resolution)
# Principal character sprites
image principal_smile = "sprites/principal/principal_smile.png"       # 832x1216 sprite
image principal_neutral = "sprites/principal/principal_neutral.png"   # 832x1216 sprite
image principal_curious = "sprites/principal/principal_curious.png"   # 832x1216 sprite

# Shion character sprites (832x1216 resolution)

# Emotions - complete set of Shion's expressions
image shion_angry = "sprites/shion/shion_angry.png"                   # 832x1216 sprite
image shion_aroused = "sprites/shion/shion_aroused.png"               # 832x1216 sprite
image shion_confused = "sprites/shion/shion_confused.png"             # 832x1216 sprite
image shion_determined = "sprites/shion/shion_determined.png"         # 832x1216 sprite
image shion_disgusted = "sprites/shion/shion_disgusted.png"           # 832x1216 sprite
image shion_embarrassed = "sprites/shion/shion_embarrassed.png"       # 832x1216 sprite
image shion_excited = "sprites/shion/shion_excited.png"               # 832x1216 sprite
image shion_happy = "sprites/shion/shion_happy.png"                   # 832x1216 sprite
image shion_hurt = "sprites/shion/shion_hurt.png"                     # 832x1216 sprite
image shion_irritated = "sprites/shion/shion_irritated.png"           # 832x1216 sprite
image shion_laughing = "sprites/shion/shion_laughing.png"             # 832x1216 sprite
image shion_love = "sprites/shion/shion_love.png"                     # 832x1216 sprite
image shion_nervous = "sprites/shion/shion_nervous.png"               # 832x1216 sprite
image shion_neutral = "sprites/shion/shion_neutral.png"               # 832x1216 sprite
image shion_playful = "sprites/shion/shion_playful.png"               # 832x1216 sprite
image shion_sad = "sprites/shion/shion_sad.png"                       # 832x1216 sprite
image shion_scared = "sprites/shion/shion_scared.png"                 # 832x1216 sprite
image shion_shy = "sprites/shion/shion_shy.png"                       # 832x1216 sprite
image shion_smug = "sprites/shion/shion_smug.png"                     # 832x1216 sprite
image shion_surprised = "sprites/shion/shion_surprised.png"           # 832x1216 sprite
image shion_thinking = "sprites/shion/shion_thinking.png"             # 832x1216 sprite
image shion_tired = "sprites/shion/shion_tired.png"                   # 832x1216 sprite
image shion_worried = "sprites/shion/shion_worried.png"               # 832x1216 sprite

# MC character sprites (832x1216 resolution)
image mc_angry = "sprites/mc/mc_angry.png"                # 832x1216 sprite
image mc_confused = "sprites/mc/mc_confused.png"          # 832x1216 sprite
image mc_curious = "sprites/mc/mc_curious.png"            # 832x1216 sprite
image mc_disgusted = "sprites/mc/mc_disgusted.png"        # 832x1216 sprite
image mc_embarrassed = "sprites/mc/mc_embarrassed.png"    # 832x1216 sprite
image mc_excited = "sprites/mc/mc_excited.png"            # 832x1216 sprite
image mc_happy = "sprites/mc/mc_happy.png"                # 832x1216 sprite
image mc_hurt = "sprites/mc/mc_hurt.png"                  # 832x1216 sprite
image mc_laughing = "sprites/mc/mc_laughing.png"          # 832x1216 sprite
image mc_nervous = "sprites/mc/mc_nervous.png"            # 832x1216 sprite
image mc_neutral = "sprites/mc/mc_neutral.png"            # 832x1216 sprite
image mc_sad = "sprites/mc/mc_sad.png"                    # 832x1216 sprite
image mc_scared = "sprites/mc/mc_scared.png"              # 832x1216 sprite
image mc_shy = "sprites/mc/mc_shy.png"                    # 832x1216 sprite
image mc_smug = "sprites/mc/mc_smug.png"                  # 832x1216 sprite
image mc_surprised = "sprites/mc/mc_surprised.png"        # 832x1216 sprite
image mc_thinking = "sprites/mc/mc_thinking.png"          # 832x1216 sprite
image mc_tired = "sprites/mc/mc_tired.png"                # 832x1216 sprite
image mc_worried = "sprites/mc/mc_worried.png"            # 832x1216 sprite

# Sound effects and music
define audio.piano_melody = "audio/piano_melody.mp3"
define audio.distant_piano = "audio/distant_piano.mp3"
define audio.footsteps = "audio/footsteps.mp3"
define audio.school_ambience = "audio/school_ambience.mp3"

# Variables
default piano_or_art = "piano" # Can be changed based on story preferences

# Start the visual novel
label start:
    # Player chooses name and gender
    python:
        name = renpy.input("What is your name?", length=20)
        name = name.strip()
        if not name:
            name = "Haru" # Default name if none provided
    
    # Transition to the school
    play sound school_ambience loop
    scene bg school_exterior with fade
    pause 1.0 # Pause to establish setting
    
    # Introduction narration - no sprites during inner thoughts
    thoughts "Today marks the beginning of my new life at Sakuragaoka High School."
    thoughts "Mid-semester transfers are always awkward, but I've gotten used to it over the years."
    
    show mc_tired at center_sprite
    
    thoughts "This is the third school in four years because of mom's job. I've learned to keep to myself."
    
    hide mc_tired with dissolve
    
    # Meet the principal
    play sound footsteps
    pause 1.0
    show principal_smile at center_sprite with dissolve
    
    principal "Welcome to Sakuragaoka High School, [name]-san. I'm Principal Yamada."
    
    show mc_neutral at left_sprite with dissolve
    
    principal "We're delighted to have you join us, even if it is mid-semester."
    principal "Let me show you around the campus before introducing you to your class."
    
    mc "Thank you, Principal Yamada."
    
    # Walking through hallways - hide sprites before scene change
    hide mc_neutral
    hide principal_smile
    scene bg school_hallway with dissolve
    play sound footsteps
    
    show principal_neutral at right_sprite with dissolve
    show mc_neutral at left_sprite with dissolve
    
    principal "This hallway connects to most of our second-year classrooms."
    
    show principal_neutral at center_sprite with move
    
    principal "The science labs are on the third floor, and club rooms are primarily in the east wing."
    
    show mc_thinking at left_sprite
    
    # Hide before thoughts
    hide principal_neutral
    thoughts "The principal continues explaining the school layout, but my attention begins to drift."
    thoughts "Another new school, another set of walls and rules to memorize."
    
    # The crucial first encounter
    stop sound fadeout 1.0
    play sound distant_piano fadein 1.0
    
    show mc_curious at left_sprite
    
    # No sprites during thoughts
    hide mc_thinking
    thoughts "As we walk down the corridor, a faint sound catches my attention."
    
    # Conditional for piano or art
    if piano_or_art == "piano":
        thoughts "A melody. Soft and melancholic, drifting through a partially open door."
        
        show mc_curious at center_sprite with move
        show principal_neutral at right_sprite with dissolve
        
        thoughts "I slow my pace, drawn to the music like a magnet."
        
        show principal_curious at right_sprite
        principal "Hmm? Did you hear something interesting, [name]-san?"
        
        show mc_nervous at center_sprite
        mc "I thought I heard... music."
        
        # Hide sprites before scene change
        hide mc_nervous
        hide principal_curious
        stop sound fadeout 1.0
        scene bg music_room_door with dissolve
        pause 1.5 # Dramatic pause before seeing through the door
        
        thoughts "Through the window of the music room door, I see someone sitting at the piano."
        
        play sound piano_melody fadein 2.0
        pause 2.0 # Let the player hear the music
        
        scene bg music_room with dissolve
        show shion_play_piano_side at center_sprite with dissolve
        pause 1.5 # Pause to show Shion playing from a distance
        
        thoughts "Their fingers dance across the keys with practiced precision, creating a haunting melody that seems to reach directly into my chest."
        
        hide shion_play_piano_side
        scene bg music_room_door with dissolve
        show mc_surprised at center_sprite with dissolve
        
        thoughts "I stop walking completely, transfixed by both the music and its creator."
        
    else:
        thoughts "As we pass by the art room, something catches my eye through the window."
        
        show mc_curious at center_sprite with move
        show principal_neutral at right_sprite with dissolve
        
        thoughts "I slow my pace, wondering what drew my attention."
        
        show principal_curious at right_sprite
        principal "Is something the matter, [name]-san?"
        
        show mc_shy at center_sprite
        mc "I just noticed someone in that room."
        
        # Hide sprites before scene change
        hide mc_shy
        hide principal_curious
        scene bg art_room_door with dissolve # Using proper art room background
        pause 1.5 # Dramatic pause before seeing through the door
        
        thoughts "Through the window, I see a student working intently at an easel."
        
        scene bg art_room with dissolve # Using proper art room background
        show shion_painting at center_sprite with dissolve # Using proper art pose
        pause 1.5 # Pause to show Shion painting from a distance
        
        thoughts "A student is working on an intricate painting, their brush moving with precision and passion."
        
        thoughts "The artwork seems to capture something I can't quite name - a feeling of longing and beauty intertwined."
        
        hide shion_painting
        scene bg art_room_door with dissolve
        show mc_surprised at center_sprite with dissolve
        
        thoughts "I slow my pace, drawn to the window to get a better look."
    
    # The eye contact moment - critical for establishing connection
    if piano_or_art == "piano":
        stop sound
        thoughts "The music stops abruptly."
    else:
        thoughts "Their brush pauses mid-stroke."
    
    # Hide sprites before scene change
    hide mc_surprised
    if piano_or_art == "piano":
        scene bg music_room with dissolve
    else:
        scene bg art_room with dissolve
    show shion_surprised at center_sprite with dissolve
    pause 2.0 # Dramatic pause for the first real look at Shion
    
    thoughts "They look up, sensing my presence, and our eyes meet through the glass."
    
    show shion_curious at center_sprite
    pause 1.5 # Lingering eye contact moment
    
    thoughts "For a brief moment, everything else fades away."
    
    thoughts "There's something in their gaze—surprise, curiosity, perhaps a flicker of recognition despite us being strangers."
    
    thoughts "The moment stretches, hanging between us like an unspoken question."
    
    # The interruption
    play sound footsteps
    show principal_neutral at left_sprite with moveinleft
    
    show mc_embarrassed at right_sprite with dissolve
    
    principal "Ah, that's Mizuki-san, one of our most talented students."
    
    thoughts "The spell breaks. I tear my eyes away, suddenly aware that I've been staring."
    
    show mc_shy at right_sprite
    
    principal "We should continue, [name]-san. There's still much to see, and your homeroom teacher is expecting us soon."
    
    show shion_curious at center_sprite
    
    # Subtle acknowledgment from Shion
    thoughts "Before turning to leave, I notice Mizuki-san give me a small, almost imperceptible nod."
    
    # Moving on - hide sprites before scene change
    hide mc_shy
    hide principal_neutral
    hide shion_curious
    scene bg school_hallway with dissolve
    show principal_neutral at right_sprite with dissolve
    show mc_thinking at left_sprite with dissolve
    
    thoughts "As we walk away, the melody lingers in my mind—or perhaps it's the memory of those eyes."
    
    principal "Next, let me show you the library..."
    
    thoughts "The principal's voice fades into background noise as I glance back toward the music room."
    
    show mc_curious at left_sprite
    
    thoughts "Something tells me this won't be our last encounter."
    
    # End of Scene 1
    # This would transition to Scene 2: Silent Integration

    # For testing purposes, end here
    return