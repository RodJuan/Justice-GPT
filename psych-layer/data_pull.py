import pandas as pd
import os

def generate_synthetic_data():
    # 1 = Coacción/Falsa (Tentativa, poca memoria sensorial, presión externa)
    # 0 = Genuina (Detallada, sensorial, propiedad de la narrativa)
    data = [
        {"statement": "I guess I was there, maybe I did it, I don't really remember the details.", "label": 1},
        {"statement": "The rain was hitting the windshield so hard I could barely see the red tail lights of the truck.", "label": 0},
        {"statement": "They told me if I just signed the paper I could go home, so I agreed with their story.", "label": 1},
        {"statement": "I remember the cold metal of the door handle and the smell of wet pavement as I ran.", "label": 0},
        {"statement": "I'm not sure, I think it happened the way the officer described it. I just wanted the room to stop spinning.", "label": 1},
        {"statement": "I saw a man in a yellow hoodie drop a black backpack near the trash bin and then walk fast toward the exit.", "label": 0},
        {"statement": "Maybe I held the weapon, I was so tired I don't know what was real anymore.", "label": 1},
        {"statement": "I was eating a slice of cold pizza and watching the news when I heard the glass shatter in the kitchen.", "label": 0},
        {"statement": "If you say I was there, then I must have been there. I trust your records more than my memory.", "label": 1},
        {"statement": "The dog wouldn't stop barking at the fence, that's what woke me up before the sirens started.", "label": 0},
        {"statement": "I just said yes because I couldn't stand the shouting anymore. I wanted the lights out of my face.", "label": 1},
        {"statement": "I noticed the neon sign was flickering, casting a blue light over the entire parking lot.", "label": 0},
        {"statement": "I suppose I could have been the one, everything is a blur and I feel so guilty.", "label": 1},
        {"statement": "I remember the sharp sting of the wind on my cheeks as I waited for the bus at 11:45 PM.", "label": 0},
        {"statement": "The detective said my friend already confessed, so I thought I should just confess too.", "label": 1},
        {"statement": "I had a headache from the loud music at the cafe, so I left early through the side door.", "label": 0},
        {"statement": "I think I saw the gun, but only because they showed me the picture so many times.", "label": 1},
        {"statement": "The floorboards creaked under my feet as I walked toward the back of the dark hallway.", "label": 0},
        {"statement": "They kept saying I was a liar until I started believing I was lying about my own innocence.", "label": 1},
        {"statement": "I was wearing my old sneakers, the ones with the hole in the toe, and they were soaked from the puddles.", "label": 0},
        {"statement": "It's possible I was angry enough to do it, I don't know, my head feels heavy.", "label": 1},
        {"statement": "I saw the reflection of the moon in the lake, it was a perfectly still and quiet night.", "label": 0},
        {"statement": "I repeated the words they told me to say because they promised me I'd see my lawyer afterward.", "label": 1},
        {"statement": "The keys were cold in my hand and I struggled to find the right one for the deadbolt.", "label": 0},
        {"statement": "I don't remember the details, but if the evidence says it was me, then it was me.", "label": 1},
        {"statement": "I heard the distinct sound of a bike chain clicking as someone rode past my window.", "label": 0},
        {"statement": "They told me my DNA was there, so I figured I must have forgotten what I did.", "label": 1},
        {"statement": "I remember the taste of the copper in my mouth after I fell and hit my face on the curb.", "label": 0},
        {"statement": "I just signed where they pointed. I didn't even read it. I just wanted to sleep.", "label": 1},
        {"statement": "The cat was sitting on the porch, staring at the empty street when the black car drove by.", "label": 0}
    ]
    
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df = pd.DataFrame(data)
    df.to_csv('data/coercion_dataset.csv', index=False)
    print(f"Dataset created with {len(data)} examples in /data/coercion_dataset.csv")

if __name__ == "__main__":
    generate_synthetic_data()
