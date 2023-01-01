import os


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(path, contents=''):
    with open(path, 'w') as f:
        f.write(contents)


def create_project_structure():
    # Create top-level directories
    create_directory('project')
    create_directory('project/src')
    create_directory('project/tests')
    create_directory('project/assets')
    create_directory('project/assets/graphics')
    create_directory('project/assets/graphics/sprites')
    create_directory('project/assets/graphics/tilemaps')
    create_directory('project/assets/audio')
    create_directory('project/assets/audio/sound_effects')
    create_directory('project/assets/audio/music')
    create_directory('project/assets/levels')
    create_directory('project/assets/tools')
    create_directory('project/assets/tools/templates')

    # Create files
    create_file('project/.gitignore')
    create_file('project/requirements.txt')
    create_file('project/setup.py')
    create_file('project/tree.md')

    # Create src directory structure
    create_directory('project/src/game')
    create_directory('project/src/game/graphics')
    create_directory('project/src/game/audio')
    create_directory('project/src/game/input')
    create_directory('project/src/game/objects')
    create_directory('project/src/game/levels')
    create_directory('project/src/tools')
    create_file('project/src/main.py')
    create_file('project/src/game/__init__.py')
    create_file('project/src/game/game.py')
    create_file('project/src/game/game_test.py')
    create_file('project/src/game/graphics/__init__.py')
    create_file('project/src/game/graphics/sprite.py')
    create_file('project/src/game/graphics/sprite_test.py')
    create_file('project/src/game/graphics/tilemap.py')
    create_file('project/src/game/graphics/tilemap_test.py')
    create_file('project/src/game/audio/__init__.py')
    create_file('project/src/game/audio/sound.py')
    create_file('project/src/game/audio/sound_test.py')
    create_file('project/src/game/audio/music.py')
    create_file('project/src/game/audio/music_test.py')
    create_file('project/src/game/input/__init__.py')
    create_file('project/src/game/input/controller.py')
    create_file('project/src/game/input/controller_test.py')
    create_file('project/src/game/input/keyboard.py')
    create_file('project/src/game/input/keyboard_test.py')
    create_file('project/src/game/objects/__init__.py')
    create_file('project/src/game/objects/character.py')
    create_file('project/src/game/objects/character_test.py')
    create_file('project/src/game/objects/item.py')
    create_file('project/src/game/objects/item_test.py')
    create_file('project/src/game/levels/__init__.py')
    create_file('project/src/game/levels/level.py')
    create_file('project/src/game/levels/level_test.py')
    create_file('project/src/game/levels/world.py')
    create_file('project/src/game/levels/world_test.py')
    create_file('project/src/tools/__init__.py')
    create_file('project/src/tools/editor.py')
    create_file('project/src/tools/editor_test.py')

    # Create tests directory structure
    create_directory('project/tests/game')
    create_directory('project/tests/game/graphics')
    create_directory('project/tests/game/audio')
    create_directory('project/tests/game/input')
    create_directory('project/tests/game/objects')
    create_directory('project/tests/game/levels')
    create_directory('project/tests/tools')
    create_file('project/tests/test_main.py')
    create_file('project/tests/test_game.py')
    create_file('project/tests/test_graphics.py')
    create_file('project/tests/test_audio.py')
    create_file('project/tests/test_input.py')
    create_file('project/tests/test_objects.py')
    create_file('project/tests/test_levels.py')
    create_file('project/tests/test_tools.py')
