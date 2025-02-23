
music_notes = ["A", "A#","B","C", "C#", "D", "D#", "E", "F","F#", "G", "G#"]

major_scale_formula = ["W","W","H","W","W","W","H"]
minor_scale_formula = ["W","H","W","W","H","W","W"]

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
    

def whole_step_after_note(current_note: str) -> str:
    current_note_index_in_music_notes = music_notes.index(current_note)
    whole_step_after = (current_note_index_in_music_notes + 2) % 12
    return music_notes[whole_step_after]

def half_step_after_note(current_note: str) -> str:
    current_note_index_in_music_notes = music_notes.index(current_note)
    half_step_after = (current_note_index_in_music_notes + 1) % 12
    return music_notes[half_step_after]



def generate_major_scale(key: str) -> str:
    result = []
    
    current_key = key
    result.append(current_key)
    
    for step in major_scale_formula:
        if step == "W":
            current_key = whole_step_after_note(current_key)
        else:
            current_key = half_step_after_note(current_key)
            
        result.append(current_key)
            
    return "".join(result)
            
        
def generate_minor_scale(key: str) -> str:
    result = []
    
    
    
    current_key = key
    result.append(current_key)
    
    for step in minor_scale_formula:
        if step == "W":
            current_key = whole_step_after_note(current_key)
        else:
            current_key = half_step_after_note(current_key)
            
        result.append(current_key)
            
    return "".join(result)

lol = "C"

print(generate_minor_scale("C"))