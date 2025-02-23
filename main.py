music_notes = ["A", "A#","B","C", "C#", "D", "D#", "E", "F","F#", "G", "G#"]
major_scale_formula = ["W","W","H","W","W","W","H"]
minor_scale_formula = ["W","H","W","W","H","W","W"]
minor_scales_that_use_flats = {"D","G","C","F","Ab","Eb","Bb"}
major_scales_that_use_flats = {"F","Bb","Eb","Ab","Db"}
major_scales_that_use_sharps = {"F#","B","E","A","D","G","A#","C#","G#"}

major_keys_that_should_be_converted = {"D#","E#", "A#", "B#", "C#", "G#", "Cb", "Fb"}

# D# maj should become Eb maj
# E# maj should become F major
# A# maj should become Bb major
# B# maj should become C major
# C# maj should become Db major
# G# maj should be Ab major


major_key_conversion_map = {
    "A#": "Bb",
    "C#": "Db",
    "D#": "Eb",
    "F#": "Gb",
    "G#": "Ab",
    "B#": "C",
    "E#": "F",
    "Cb": "B",
    "Fb": "E"
}

flat_to_sharp_conversion_map = {
    "Bb": "A#",
    "Db": "C#",
    "Eb": "D#",
    "Gb": "F#",
    "Ab": "G#"
}

def is_sharp(note: str) -> bool:
    if len(note) == 1:
        return False
    return note[1] == "#"

def whole_step_after_note(current_note: str) -> str:
    if current_note in flat_to_sharp_conversion_map:
        current_note = flat_to_sharp_conversion_map[current_note]
    
    current_note_index_in_music_notes = music_notes.index(current_note)
    whole_step_after = (current_note_index_in_music_notes + 2) % 12
    return music_notes[whole_step_after]

def half_step_after_note(current_note: str) -> str:
    if current_note in flat_to_sharp_conversion_map:
        current_note = flat_to_sharp_conversion_map[current_note]
        
    current_note_index_in_music_notes = music_notes.index(current_note)
    half_step_after = (current_note_index_in_music_notes + 1) % 12
    return music_notes[half_step_after]


def generate_major_scale(key: str) -> list[str]:
    result = []
    
    current_key = key
    
    if current_key in major_keys_that_should_be_converted:
        current_key = major_key_conversion_map[current_key]
        
    uses_flats = key_uses_flats(current_key)
    
    result.append(current_key)
    
    for step in major_scale_formula:
        if step == "W":
            current_key = whole_step_after_note(current_key)
        else:
            current_key = half_step_after_note(current_key)

        if uses_flats and len(current_key) == 2 and current_key[1] == "#":
            current_key = major_key_conversion_map[current_key]
            
        result.append(current_key)
    
    if key == "F#":
        desired_index = result.index("F")
        result[desired_index] = "E#"
    
    return result

def key_uses_flats(key: str):
    if key == "F":
        return True
    if len(key) == 1:
        return False
    return key[1] == "b"
            
def output_scale_clean(scale: str):
    print("\t\tThe " + scale[0] + " major scale:")
    for note in scale:
        print("%3s   " % (note), end="")
    print()
    print()
        
def generate_minor_scale(key: str) -> list[str]:
    result = []
    
    current_key = key
    result.append(current_key)
    
    for step in minor_scale_formula:
        if step == "W":
            current_key = whole_step_after_note(current_key)
        else:
            current_key = half_step_after_note(current_key)
            
        result.append(current_key)
    return result

for note in music_notes:
    output_scale_clean(generate_major_scale(note))