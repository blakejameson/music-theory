from typing import Union

music_notes = ["A", "A#","B","C", "C#", "D", "D#", "E", "F","F#", "G", "G#"]
major_scale_formula = ["W","W","H","W","W","W","H"]
minor_scale_formula = ["W","H","W","W","H","W","W"]
harmonic_minor_scale_formula = ["W","H","W","W", "H","T","H"]
melodic_minor_scale_formula = ["W","H","W","W","W","W","H"]

major_scale_roman_numerals = ["I","ii","iii", "IV", "V", "vi", "vii\u00B0"]
minor_scale_roman_numerals = ["i","ii\u00B0","III","iv","v","VI","VII"]

valid_root_notes = ["A", "B", "C", "D", "E", "F", "G", "A#", "C#", "D#", "F#", "G#", "Ab", "Bb", "Db", "Eb", "Gb"]

supported_chord_types = ["m", "min", "maj",
          "maj7",
          "min7",
          "m7",
          "7",
          "sus2",
          "sus4",
          "5",
          "add9",
          "6",
          "maj6",
          "maj9",
          "min6",
          "m6",
          "m9",
          "min9"]


def generate_all_chords() -> set[str]:
    all_chords = set()
    
    for root_note in valid_root_notes:
        for type in supported_chord_types:
            chord = root_note + type
            all_chords.add(chord)
        
        all_chords.add(root_note)
    return all_chords
        

all_valid_chords_supported: Union[set, None] = None
all_valid_chords_supported = generate_all_chords()



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


def display_options() -> None:
    
    print("\nHere are the following options:\n\n1) Explore a specific key.\n2) Learn the notes of a scale.\n3) Learn the notes in a chord.\n")
    
def learn_notes_in_chord() -> None:
    
    print("In a moment, you will enter the chord of your choice. \n\nThe following types of chords are supported and examples of your input when entering the chord is on the right:\n")
    
    chord_types = ["* Major",
          "* Minor",
          "* Major 7 (maj7)",
          "* Minor 7 (min7 or m7)",
          "* Dominant 7 (7)",
          "* Suspended 2nd (sus2)",
          "* Suspended 4th (sus4)",
          "* Fifth (5)",
          "* Added 9th (add9)",
          "* Major 6 (6 or maj6)",
          "* Major 9 (maj9)",
          "* Minor 6 (min6 or m6)",
          "* Minor 9 (min9 or m6)"]
    print("%-30s %s "% ("Chord Type:", "Input Examples:\n"))
    examples = ["C or Cmaj, Ab or Abmaj, F# or F#maj", "Cm or Cmin, Abm or Abmin, F#m or F#min", "Cmaj7, Abmaj7, F#maj7", "Cmin7 or Cm7, Abmin7 or Abm7, F#min7 or F#m7", "C7, Ab7, F#7", "Csus2, Absus2, F#sus2", "Csus4, Absus4, F#sus4", "C5, Ab5, F#5", "Cadd9, Abadd9, F#add9", "C6 or Cmaj6, Ab6 or Abmaj6, F#6 or F#maj6", "Cmaj9, Abmaj9, F#maj9", "Cmin6 or Cm6, Abmin6 or Abm6, F#min6 or F#m6", "Cmin9 or Cm9, Abmin9 or Abm9, F#min9 or F#m9",]
    result = "\n".join("%-30s %-10s "%(x,y) for x, y in zip(chord_types, examples))
    print(result, end="\n\n\n")
    
    # capture chord choice
    chord_choice = input("Enter a chord of your choice, and you will be returned the notes that make up that chord: \n")
    
    while not is_valid_chord(chord_choice):
        print("Invalid chord entered. Please follow the convention shown above to enter a valid chord.")
        chord_choice = input("Enter a chord: ")
        
    notes = decipher_chord_and_return_notes(chord_choice)
    print(notes)
    
    
def is_valid_chord(chord_input: str) -> bool:
    stripped_input = chord_input.strip()
    return stripped_input in all_valid_chords_supported



def decipher_chord_and_return_notes(chord: str) -> None:
    notes = None
    # This means it is A through G major
    if len(chord) == 1:
        notes = generate_major_chord(chord)
        return notes
    
    # Length 2 means it is either a minor chord (ex: Cm), a major chord (ex: F#, dominant 7, fifth, or 6 aka maj6)
    elif len(chord) == 2:
        if chord[1] == "#" or chord[1] == "b":
            notes = generate_major_chord(chord[0])
            return notes
        
        elif chord[1] == "m":
            notes = generate_minor_chord(chord[0])
            return notes
        
        elif chord[1] == "7":
            notes = generate_dominant7_chord(chord[0])
            return notes
        
        elif chord[1] == "5":
            notes = generate_5_chord(chord[0])
            return notes
        
        elif chord[1] == "6":
            notes = generate_maj6_chord(chord)
            return notes
        
    elif "maj7" in chord:
        index_maj7_starts_at = chord.find("maj7")
        
        notes = generate_major7_chord(chord[:index_maj7_starts_at])
        return notes
    
    elif "maj6" in chord:
        index_maj6_starts_at = chord.find("maj6")
        
        notes = generate_maj6_chord(chord[:index_maj6_starts_at])
        return notes
    
    elif "add9" in chord:
        index_add9_starts_at = chord.find("add9")
        
        notes = generate_add9_chord(chord[:index_add9_starts_at])
        return notes
    
    elif "maj9" in chord:
        index_maj9_starts_at = chord.find("maj9")
        
        notes = generate_major9_chord(chord[:index_maj9_starts_at])
        return notes
    
    elif "min7" in chord:
        index_min7_starts_at = chord.find("min7")
        notes = generate_minor7_chord(chord[:index_min7_starts_at])
        return notes
    
    elif "m7" in chord:
        index_min7_starts_at = chord.find("m7")
        notes = generate_minor7_chord(chord[:index_min7_starts_at])
        return notes
    
    elif "min6" in chord:
        index_min6_starts_at = chord.find("min6")
        notes = generate_min6_chord(chord[:index_min6_starts_at])
        return notes
    
    elif "m6" in chord:
        index_min6_starts_at = chord.find("m6")
        notes = generate_min6_chord(chord[:index_min6_starts_at])
        return notes
    

    elif "min9" in chord:
        index_min9_starts_at = chord.find("min9")
        notes = generate_minor9_chord(chord[:index_min9_starts_at])
        return notes
    
    elif "m9" in chord:
        index_min9_starts_at = chord.find("m9")
        notes = generate_minor9_chord(chord[:index_min9_starts_at])
        return notes
    
    elif "sus2" in chord:
        index_sus2_starts_at = chord.find("sus2")
        notes = generate_sus2_chord(chord[:index_sus2_starts_at])
        return notes
    
    elif "sus4" in chord:
        index_sus4_starts_at = chord.find("sus4")
        notes = generate_sus4_chord(chord[:index_sus4_starts_at])
        return notes
    
    # if dominant 7
    elif "7" in chord:
        index_7_starts_at = chord.find("7")
        notes = generate_dominant7_chord(chord[:index_7_starts_at])
        return notes
    
    # if 5th
    elif "5" in chord:
        index_5_starts_at = chord.find("5")
        notes = generate_5_chord(chord[:index_5_starts_at])
        return notes
    
    elif "maj" in chord:
        index_maj_starts_at = chord.find("maj")
        notes = generate_major_chord(chord[:index_maj_starts_at])
        return notes
        
        
    
def main():
    while True:
        learn_notes_in_chord()
    
    while True:
        display_options()
        user_decision = input()
        
        while user_decision not in {"1","2","3"}:
            print("Please select a valid option: ")
            user_decision = input()
            
        if user_decision == 3:
            pass
            
        
        
        
        selection = input("Enter your key of choice: ")

        choice = input("Enter major to see the major scale or minor to see the minor scale: ")
        
        if choice == "major":
            output_scale_clean(generate_major_scale(selection), "major")
        else:
            output_scale_clean(generate_minor_scale(selection), "minor")


display_options()
main()