music_notes = ["A", "A#","B","C", "C#", "D", "D#", "E", "F","F#", "G", "G#"]
major_scale_formula = ["W","W","H","W","W","W","H"]
minor_scale_formula = ["W","H","W","W","H","W","W"]
harmonic_minor_scale_formula = ["W","H","W","W", "H","T","H"]
melodic_minor_scale_formula = ["W","H","W","W","W","W","H"]

major_scale_roman_numerals = ["I","ii","iii", "IV", "V", "vi", "vii\u00B0"]
minor_scale_roman_numerals = ["i","ii\u00B0","III","iv","v","VI","VII"]

# need to later do harmonic minor and melodic minor roman numerals

flat_to_sharp_conversion_map = {
    "Bb": "A#",
    "Db": "C#",
    "Eb": "D#",
    "Gb": "F#",
    "Ab": "G#",
}

sharp_to_flat_conversion_map = {
    "A#": "Bb",
    "C#": "Db",
    "D#": "Eb",
    "F#": "Gb",
    "G#": "Ab"
}

def is_sharp(note: str) -> bool:
    if len(note) == 1:
        return False
    return note[1] == "#"

def whole_step_after_note(current_note: str, usesFlats: bool) -> str:
    if usesFlats and current_note in flat_to_sharp_conversion_map and not is_sharp(current_note):
        current_note = flat_to_sharp_conversion_map[current_note]

    current_note_index_in_music_notes = music_notes.index(current_note)
    whole_step_after = (current_note_index_in_music_notes + 2) % 12
    return music_notes[whole_step_after]

def half_step_after_note(current_note: str, usesFlats: bool) -> str:
    if usesFlats and current_note in flat_to_sharp_conversion_map and not is_sharp(current_note):
        current_note = flat_to_sharp_conversion_map[current_note]
        
    current_note_index_in_music_notes = music_notes.index(current_note)
    half_step_after = (current_note_index_in_music_notes + 1) % 12
    return music_notes[half_step_after]

def three_step_after_note(current_note: str, usesFlats: bool) -> str:
    if usesFlats and current_note in flat_to_sharp_conversion_map and not is_sharp(current_note):
        current_note = flat_to_sharp_conversion_map[current_note]
        
    current_note_index_in_music_notes = music_notes.index(current_note)
    half_step_after = (current_note_index_in_music_notes + 3) % 12
    return music_notes[half_step_after]


def major_key_uses_flats(key: str):
    if key == "F":
        return True
    if len(key) == 1:
        return False
    return key[1] == "b"

def minor_key_uses_flats(key: str):
    natural_keys_with_flats = {"D","G","C","F"}
    if key in natural_keys_with_flats:
        return True
    
    if len(key) == 1:
        return False
    return key[1] == "b"
            
def output_scale_clean(scale: str, mode: str):
    print("\t\tThe " + scale[0] + f" {mode} scale:")
    for note in scale:
        print("%3s   " % (note), end="")
    print()
    print()
        
def generate_major_scale(key: str) -> list[str]:
    result = []
    current_key = key
    uses_flats = major_key_uses_flats(current_key)
    result.append(current_key)
    
    for step in major_scale_formula:
        if step == "W":
            current_key = whole_step_after_note(current_key, uses_flats)
        else:
            current_key = half_step_after_note(current_key, uses_flats)

        if uses_flats and is_sharp(current_key):
            current_key = sharp_to_flat_conversion_map[current_key]
        result.append(current_key)
    
    return result

def generate_minor_scale(key: str) -> list[str]:
    result = []
    current_key = key
    uses_flats = minor_key_uses_flats(current_key)
    
    result.append(current_key)
    
    for step in minor_scale_formula:
        if step == "W":
            current_key = whole_step_after_note(current_key, uses_flats)
        else:
            current_key = half_step_after_note(current_key, uses_flats)
    
        if uses_flats and is_sharp(current_key):
            current_key = sharp_to_flat_conversion_map[current_key]
        result.append(current_key)
    return result

def generate_harmonic_minor_scale(key: str) -> list[str]:
    result = []
    current_key = key
    uses_flats = minor_key_uses_flats(current_key)
    
    result.append(current_key)
    
    for step in harmonic_minor_scale_formula:
        if step == "W":
            current_key = whole_step_after_note(current_key, uses_flats)
        elif step == "H":
            current_key = half_step_after_note(current_key, uses_flats)
            
        else:
            current_key = three_step_after_note(current_key, uses_flats)
            
    
        if uses_flats and is_sharp(current_key):
            current_key = sharp_to_flat_conversion_map[current_key]
        result.append(current_key)
        
        
    ## G harmonic minor and D harmonic minor have a sharp note at position 7, 
    # despite having flats in scale
    if key == "G" or key == "D":
        result[6] = flat_to_sharp_conversion_map[result[6]]
    
    return result

def generate_melodic_minor_scale(key: str) -> list[str]:
    result = []
    current_key = key
    uses_flats = minor_key_uses_flats(current_key)
    
    result.append(current_key)
    
    for step in melodic_minor_scale_formula:
        if step == "W":
            current_key = whole_step_after_note(current_key, uses_flats)
        else:
            current_key = half_step_after_note(current_key, uses_flats)
    
        if uses_flats and is_sharp(current_key):
            current_key = sharp_to_flat_conversion_map[current_key]
        result.append(current_key)
        
    ## G melodic minor and D melodic minor have a sharp note at position 7, 
    # despite having flats in scale
    if key == "G" or key == "D":
        result[6] = flat_to_sharp_conversion_map[result[6]]
    
    return result

def generate_major_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    
    list_notes = [major_scale[0], major_scale[2], major_scale[4]]
    return "".join(list_notes)

def generate_major7_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    
    list_notes = [major_scale[0], major_scale[2], major_scale[4], major_scale[6]]
    return "".join(list_notes)

def generate_major9_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    
    list_notes = [major_scale[0], major_scale[2], major_scale[4], major_scale[6], major_scale[1]]
    return "".join(list_notes)

def generate_minor_chord(root: str) -> str:
    minor_scale = generate_minor_scale(root)
    
    list_notes = [minor_scale[0], minor_scale[2], minor_scale[4]]
    return "".join(list_notes)

def generate_minor7_chord(root: str) -> str:
    minor_scale = generate_minor_scale(root)
    
    list_notes = [minor_scale[0], minor_scale[2], minor_scale[4], minor_scale[6]]
    return "".join(list_notes)

def generate_minor9_chord(root: str) -> str:
    minor_scale = generate_minor_scale(root)
    major_scale = generate_major_scale(root)
    
    list_notes = [minor_scale[0], minor_scale[2], minor_scale[4], minor_scale[6], major_scale[1]]
    return "".join(list_notes)


def generate_sus2_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    
    list_notes = [major_scale[0], major_scale[1], major_scale[4]]
    return "".join(list_notes)

def generate_sus4_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    
    list_notes = [major_scale[0], major_scale[3], major_scale[4]]
    return "".join(list_notes)

def generate_dominant7_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    minor_scale = generate_minor_scale(root)
    
    list_notes = [major_scale[0], major_scale[2], major_scale[4], minor_scale[6]]
    return "".join(list_notes)

def generate_5_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    
    list_notes = [major_scale[0], major_scale[4]]
    return "".join(list_notes)

def generate_add9_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    
    list_notes = [major_scale[0], major_scale[2], major_scale[4], major_scale[1]]
    return "".join(list_notes)

def generate_maj6_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    
    list_notes = [major_scale[0], major_scale[2], major_scale[4], major_scale[5]]
    return "".join(list_notes)

def generate_min6_chord(root: str) -> str:
    major_scale = generate_major_scale(root)
    
    minor_scale = generate_minor_scale(root)
    
    list_notes = [minor_scale[0], minor_scale[2], minor_scale[4], major_scale[5]]
    return "".join(list_notes)

def main():
    while True:
        selection = input("Enter your key of choice: ")

        choice = input("Enter major to see the major scale or minor to see the minor scale: ")
        
        if choice == "major":
            output_scale_clean(generate_major_scale(selection), "major")
        else:
            output_scale_clean(generate_minor_scale(selection), "minor")


print(generate_minor9_chord("C"))