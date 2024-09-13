init python:
    
    class Dummy: #a dummy class used in place of a battle. Normally this should be integrated with Jake's battle engine, instead of using a dummy class.
        def __init__(self,won):
            self.won = won
            
        
    ari_battle = Dummy(False)
    #sprite arrays should always be in north, south, east, west order.
    map_on = False #Is a map being displayed? This governs whether the "yesno" screen is modal.
    
    #SPRITES
    null_sprites = [["null_tile.png"],
        ["null_tile.png"], 
        ["null_tile.png"], 
        ["null_tile.png"],
        (128,128)]
    
    
    virgil_sprites = [["spVirgil.png"],
        ["spVirgil.png"], 
        ["spVirgil.png"], 
        ["spVirgil.png"],
        (45,75)]
    homer_sprites = [["spHomer.png"],
        ["spHomer.png"], 
        ["spHomer.png"], 
        ["spHomer.png"],
        (45,75)]
    rumi_sprites = [["spRumi.png"],
        ["spRumi.png"], 
        ["spRumi.png"], 
        ["spRumi.png"],
        (45,75)]
    shakespeare_sprites = [["spShakespeare.png"],
        ["spShakespeare.png"], 
        ["spShakespeare.png"], 
        ["spShakespeare.png"],
        (45,75)]
    poe_sprites = [["spPoe.png"],
        ["spPoe.png"], 
        ["spPoe.png"], 
        ["spPoe.png"],
        (45,75)]
    shel_sprites = [["spShel.png"],
        ["spShel.png"], 
        ["spShel.png"], 
        ["spShel.png"],
        (45,75)]
    minos_sprites = [["minos_serpent.png"],
        ["minos_serpent.png"],
        ["minos_serpent.png"],
        ["minos_serpent.png"],
        (512,512)]
    
    plutus_sprites = [["plutus_ground.png"],
        ["plutus_ground.png"],
        ["plutus_ground.png"],
        ["plutus_ground.png"],
        (384,384)]
    
    phlegyas_sprites = [["phlegyas.png"],
        ["phlegyas.png"],
        ["phlegyas.png"],
        ["phlegyas.png"],
        (256,256)]
        
        
    demon01_sprites = [["demon01_1.png", "demon01_2.png",],  #enemy sprites
        ["demon01_1.png", "demon01_2.png",], 
        ["demon01_1.png", "demon01_2.png",], 
        ["demon01_1.png", "demon01_2.png",],
        (78,106)]
    
    victim_sprites = [["sprite_victim.png"],
        ["sprite_victim.png"],
        ["sprite_victim.png"],
        ["sprite_victim.png"],
        (36,36)]
    
    lovecraft_sprites = [["lovecraft_sprite_trans.png"],
        ["lovecraft_sprite_trans.png"],
        ["lovecraft_sprite_trans.png"],
        ["lovecraft_sprite_trans.png"],
        (32,32)]
    
    ken_sprites =[ #player sprites
    ["spAD-N1.png", "spAD-N2.png", "spAD-N2.png","spAD-N1.png","spAD-N3.png","spAD-N3.png",],
    ["spAD-S1.png", "spAD-S2.png", "spAD-S2.png","spAD-S1.png","spAD-S3.png","spAD-S3.png",],
    ["spAD-E1.png", "spAD-E2.png", "spAD-E2.png","spAD-E1.png","spAD-E2.png","spAD-E2.png",],
    ["spAD-W1.png", "spAD-W2.png", "spAD-W2.png","spAD-W1.png","spAD-W2.png","spAD-W2.png",],
    (80,64)
    ]
    
    villager_sprites = [ #villager
    ["bee-1.png", "bee-2.png", "bee-3.png", "bee-2.png", "bee-1.png","bee-4.png", "bee-5.png","bee-4.png"],
    ["bee-1.png", "bee-2.png", "bee-3.png", "bee-2.png", "bee-1.png","bee-4.png", "bee-5.png","bee-4.png"],
    ["bee-1.png", "bee-2.png", "bee-3.png", "bee-2.png", "bee-1.png","bee-4.png", "bee-5.png","bee-4.png"],
    ["bee-1.png", "bee-2.png", "bee-3.png", "bee-2.png", "bee-1.png","bee-4.png", "bee-5.png","bee-4.png"],
    (70,80)
    ]
    
    trainer_sprites =[ #trainer sprites
    ["trainer_n1.png", "trainer_n2.png", "trainer_n2.png", "trainer_n1.png", "trainer_n3.png", "trainer_n3.png",],
    ["trainer_s1.png", "trainer_s2.png", "trainer_s2.png", "trainer_s1.png", "trainer_s3.png", "trainer_s3.png",],
    ["trainer_e1.png", "trainer_e2.png", "trainer_e2.png", "trainer_e1.png", "trainer_e2.png", "trainer_e2.png",],
    ["trainer_w1.png", "trainer_w2.png", "trainer_w2.png", "trainer_w1.png", "trainer_w2.png", "trainer_w2.png",],
    (32,32)
    ]
    
    #TILESETS
    gateway_tiles = [
    ["C", "wall", (128,128),None,False,None,None],
    ["L", "wall-left", (128,128),None,False,None,None],
    ["R", "wall-right", (128,128),None,False,None,None],
    ["H", "path_horz", (128,128),None, False, None,None],
    ["V", "path_vert", (128,128),None, False, None,None],
    ["J", "path_junc", (128,128),None, False, None,None],
    ["G", "path_gate", (128,128),None, False, None,None],
    ["g", "grass", (128,128),None, False, None,None],
    ["t", "wall-right-abandon", (128,128),None, False, None,None],
    ["y", "wall-right-allhope", (128,128),None, False, None,None],
    ]
    
    gateway_layout =[
    "CCCCCCCCCCCCCCC",
    "Looooooooooooot",
    "L+ooooooooooooo",
    "Loooooooooooooy",
    "CCCCCCCCCCCCCCC",
    ]
    
    gateway_portal_tiles = [['p', 'betrayal']]
    gateway_portals =[
    "ooooooooooooooo",
    "ooooooooooooooo",
    "oooooooooooooop",
    "ooooooooooooooo",
    "ooooooooooooooo",
    ]
    
    gateway_ground =[
    "ggggggggggggggg",
    "ggggggggggggggg",
    "HHHHHHHHHHHHHHG",
    "ggggggggggggggg",
    "ggggggggggggggg",
    ]
    
    gateway_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    gateway_villagers = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    gateway_enemies_layout =[
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    ]
    
    
    
    
    hell01_tiles = [
    ["C", "wall", (128,128),None,False,None,None],
    ["L", "wall-left", (128,128),None,False,None,None],
    ["R", "wall-right", (128,128),None,False,None,None],
    ["H", "hell_horz", (128,128),None, False, None,None],
    ["V", "hell_vert", (128,128),None, False, None,None],
    ["J", "hell_junc", (128,128),None, False, None,None],
    ["G", "path_gate", (128,128),None, False, None,None],
    ["g", "hell_stone", (128,128),None, False, None,None],
    ["t", "wall-right-abandon", (128,128),None, False, None,None],
    ["y", "wall-right-allhope", (128,128),None, False, None,None],
    ]
    
    hell01_layout =[
    "CCCCCCCCCCCCCCCCC",
    "L+ooooooooooooooR",
    "LoooooooooooooooR",
    "LoooooooooooooooR",
    "LoooooooooooooooR",
    "CCCCCCCCCCCCCCCCC",
    ]
    
    hell01_portal_tiles = [['p', 'betrayal']]
    hell01_portals =[
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    ]
    
    hell01_ground =[
    "ggggggggggggggggg",
    "ggggggggggggggggg",
    "ggggggggggggggggg",
    "ggggggggggggggggg",
    "ggggggggggggggggg",
    "ggggggggggggggggg",
    ]
    
    hell01_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    hell01_villagers = [
    ["q", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    hell01_enemies_layout =[
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "ooooooooooooooooo",
    "oooooooooooaaaaao",
    "oooooooooaaaaaaao",
    "ooooooooooooooooo",
    ]
    
    
    
    
    
    
    
    limbo_tiles = [
    ["C", "limbo_wall", (128,128),None,False,None,None],
    ["L", "limbo_wall-left", (128,128),None,False,None,None],
    ["R", "limbo_wall-right", (128,128),None,False,None,None],
    ["p", "limbo_pole", (128,128),None, False, None,None],
    ["g", "limbo_stone", (128,128),None, False, None,None],
    ["B", "void_wall",(128,128),None, False, None,None],
    ]
    
    limbo_layout =[
    "BBBBB",
    "CLoRC",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "L+ooR",
    "CCCCCCC",
    ]
    
    limbo_portal_tiles = [['q', 'limbogame']]
    limbo_portals =[
    "ooooo",
    "ooqoo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    ]
    
    limbo_ground =[
    "ggggg",
    "ggpgg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    ]
    
    limbo_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    limbo_villagers = [
    ["v",None, False, virgil_sprites,  "right", "virgiltalk"],
    ["h",None, False, homer_sprites,  "right", "homertalk"],
    ["r",None, False, rumi_sprites,  "right", "rumitalk"],
    ["s",None, False, shakespeare_sprites,  "right", "shakespearetalk"],
    ["p",None, False, poe_sprites,  "right", "poetalk"],
    ["l",None, False, shel_sprites,  "right", "sheltalk"],
    ]
    limbo_enemies_layout =[
    "ooooo",
    "ooooo",
    "ooooo",
    "ooolo",
    "ooopo",
    "oooso",
    "oooro",
    "oooho",
    "ooooo",
    "oovoo",
    "ooooo",
    ]
    
    
    
    
    
    
    limbo3_tiles = [
    ["C", "limbo_wall", (128,128),None,False,None,None],
    ["L", "limbo_wall-left", (128,128),None,False,None,None],
    ["R", "limbo_wall-right", (128,128),None,False,None,None],
    ["p", "limbo_pole", (128,128),None, False, None,None],
    ["g", "limbo_stone", (128,128),None, False, None,None],
    ["B", "void_wall",(128,128),None, False, None,None],
    ]
    
    limbo3_layout =[
    "BBBBB",
    "CLoRC",
    "Lo+oR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "CCCCC",
    ]
    
    limbo3_portal_tiles = [['q', 'limbogame']]
    limbo3_portals =[
    "ooooo",
    "ooqoo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    ]
    
    limbo3_ground =[
    "ggggg",
    "ggpgg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    ]
    
    limbo3_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    limbo3_villagers = [
    ["v",None, False, virgil_sprites,  "right", "virgiltalk"],
    ["h",None, False, homer_sprites,  "right", "homertalk"],
    ["r",None, False, rumi_sprites,  "right", "rumitalk"],
    ["s",None, False, shakespeare_sprites,  "right", "shakespearetalk"],
    ["p",None, False, poe_sprites,  "right", "poetalk"],
    ["l",None, False, shel_sprites,  "right", "sheltalk"],
    ]
    
    
    limbo3_enemies_layout =[
    "ooooo",
    "ooooo",
    "ooooo",
    "ooolo",
    "ooopo",
    "oooso",
    "oooro",
    "oooho",
    "ooooo",
    "oovoo",
    "ooooo",
    ]
    
    
    
    
    
    
    
    
    limbo2_tiles = [
    ["C", "limbo_wall", (128,128),None,False,None,None],
    ["L", "limbo_wall-left", (128,128),None,False,None,None],
    ["R", "limbo_wall-right", (128,128),None,False,None,None],
    ["p", "limbo_pole_empty", (128,128),None, False, None,None],
    ["g", "limbo_stone", (128,128),None, False, None,None],
    ["B", "void_wall",(128,128),None, False, None,None],
    ]
    
    limbo2_layout =[
    "BBBBB",
    "CLoRC",
    "Lo+oR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "LoooR",
    "CCCCC",
    ]
    
    limbo2_portal_tiles = [['q', 'minos']]
    limbo2_portals =[
    "ooooo",
    "ooqoo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    "ooooo",
    ]
    
    limbo2_ground =[
    "ggggg",
    "ggpgg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    "ggggg",
    ]
    
    limbo2_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    limbo2_villagers = [
    ["v",None, False, virgil_sprites,  "right", "virgiltalk2"],
    ["h",None, False, homer_sprites,  "right", "homertalk2"],
    ["r",None, False, rumi_sprites,  "right", "rumitalk2"],
    ["s",None, False, shakespeare_sprites,  "right", "shakespearetalk2"],
    ["p",None, False, poe_sprites,  "right", "poetalk2"],
    ["l",None, False, shel_sprites,  "right", "sheltalk2"],
    ]
    limbo2_enemies_layout =[
    "ooooo",
    "ooooo",
    "ooovo",
    "ooolo",
    "ooopo",
    "oooso",
    "oooro",
    "oooho",
    "ooooo",
    "ooooo",
    "ooooo",
    ]
    
    
    
    
    
    
    
    minos_tiles = [
    ["C", "minos_wall", (128,128),None,False,None,None],
    ["L", "minos_wall-left", (128,128),None,False,None,None],
    ["R", "minos_wall-right", (128,128),None,False,None,None],
    ["p", "limbo_pole_empty", (128,128),None, False, None,None],
    ["g", "minos_floor", (128,128),None, False, None,None],
    ["B", "void_wall",(128,128),None, False, None,None],
    ["M", "minos_serpent_up",(512,256),None, False, None,None],
    ["N", "minos_serpent_down",(512,256),None, False, None,None],
    ]
    
    minos_layout =[
    "BBBBBB",
    "CLooRC",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooRCCCCCCCCCCCCCR",
    "Looooooooooooooooo+R",
    "CCCCCCCCCCCCCCCCCCCC",
    ]
    
    minos_portal_tiles = [['q', 'minos1']]
    minos_portals =[
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "ooooooooooooooqooooo",
    "oooooooooooooooooooo",
    ]
    
    minos_ground =[
    "gggggg",
    "goooog",
    "gMooog",
    "goooog",
    "gNooog",
    "goooog",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    ]
    
    minos_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    minos_villagers = [
    ["m", (256,256), False, minos_sprites,  "right", "virgiltalk2"],
    ]
    minos_enemies_layout =[
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    
    
    
    
    
    minos1_layout =[
    "BBBBBB",
    "CLooRC",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooRCCCCCCCCCCCCCR",
    "Looooooooooooo+ooooR",
    "CCCCCCCCCCCCCCCCCCCC",
    ]
    
    
    minos1_portal_tiles = [['q', 'minos2']]
    minos1_portals =[
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "oooooooooqoooooooooo",
    "oooooooooooooooooooo",
    ]
    
    minos2_layout =[
    "BBBBBB",
    "CLooRC",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooRCCCCCCCCCCCCCR",
    "Looooooooooooo+ooooR",
    "CCCCCCCCCCCCCCCCCCCC",
    ]
    
    minos2_portal_tiles = [['q', 'minos3']]
    minos2_portals =[
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "oooooooqoooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    minos3_portal_tiles = [['q', 'minos4']]
    minos3_portals =[
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oqqqqo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    minos3_layout =[
    "BBBBBB",
    "CLooRC",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooRCCCCCCCCCCCCCR",
    "Loooo+oooooooooooooR",
    "CCCCCCCCCCCCCCCCCCCC",
    ]
    
    minos4_portal_tiles = [['q', 'minos5']]
    minos4_portals =[
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oqqqqo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    minos4_layout =[
    "BBBBBB",
    "CLooRC",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "Loo+oR",
    "LooooR",
    "LooooR",
    "LooooRCCCCCCCCCCCCCR",
    "LooooooooooooooooooR",
    "CCCCCCCCCCCCCCCCCCCC",
    ]
    
    
    
    
    
    minosend_tiles = [
    ["C", "minos_wall", (128,128),None,False,None,None],
    ["L", "minos_wall-left", (128,128),None,False,None,None],
    ["R", "minos_wall-right", (128,128),None,False,None,None],
    ["p", "limbo_pole_empty", (128,128),None, False, None,None],
    ["g", "minos_floor", (128,128),None, False, None,None],
    ["B", "void_wall",(128,128),None, False, None,None],
    ["M", "minos_serpent_up",(512,256),None, False, None,None],
    ["N", "minos_serpent_down",(512,256),None, False, None,None],
    ]
    
    minosend_layout =[
    "BBBBBB",
    "CLooRC",
    "LooooR",
    "LooooR",
    "LooooR",
    "Loo+oR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooRCCCCCCCCCCCCCR",
    "LooooooooooooooooooR",
    "CCCCCCCCCCCCCCCCCCCC",
    ]
    
    minosend_portal_tiles = [['q', 'end']]
    minosend_portals =[
    "oooooo",
    "ooqqoo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    minosend_ground =[
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    ]
    
    minosend_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    minosend_villagers = [
    ["m", (256,256), False, minos_sprites,  "right", "virgiltalk2"],
    ]
    minosend_enemies_layout =[
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    
    
    
    
    
    
    
    
    
    minosend_tiles = [
    ["C", "circleII_wall", (128,128),None,False,None,None],
    ["L", "circleII_wall-left", (128,128),None,False,None,None],
    ["R", "circleII_wall-right", (128,128),None,False,None,None],
    ["g", "circleII_stone", (128,128),None, False, None,None],
    ["B", "void_wall",(128,128),None, False, None,None],
    ]
    
    minosend_layout =[
    "BBBBBB",
    "CLooRC",
    "LooooR",
    "LooooR",
    "LooooR",
    "Loo+oR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooR",
    "LooooRCCCCCCCCCCCCCR",
    "LooooooooooooooooooR",
    "CCCCCCCCCCCCCCCCCCCC",
    ]
    
    minosend_portal_tiles = [['q', 'circleII']]
    minosend_portals =[
    "oooooo",
    "ooqqoo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    minosend_ground =[
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggg",
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    "gggggggggggggggggggg",
    ]
    
    minosend_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    minosend_villagers = [
    ["m", (256,256), False, minos_sprites,  "right", "virgiltalk2"],
    ]
    minosend_enemies_layout =[
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    
    
    
    
    
    
    
    
    
    
    
    page1_sprites = [["circleII_stone_page1.png"],
        ["circleII_stone_page1.png"],
        ["circleII_stone_page1.png"],
        ["circleII_stone_page1.png"],
        (128,128)]
    page2_sprites = [["circleII_stone_page2.png"],
        ["circleII_stone_page2.png"],
        ["circleII_stone_page2.png"],
        ["circleII_stone_page2.png"],
        (128,128)]
    page3_sprites = [["circleII_stone_page3.png"],
        ["circleII_stone_page3.png"],
        ["circleII_stone_page3.png"],
        ["circleII_stone_page3.png"],
        (128,128)]
    page4_sprites = [["circleII_stone_page4.png"],
        ["circleII_stone_page4.png"],
        ["circleII_stone_page4.png"],
        ["circleII_stone_page4.png"],
        (128,128)]
    page5_sprites = [["circleII_stone_page5.png"],
        ["circleII_stone_page5.png"],
        ["circleII_stone_page5.png"],
        ["circleII_stone_page5.png"],
        (128,128)]
    page6_sprites = [["circleII_stone_page6.png"],
        ["circleII_stone_page6.png"],
        ["circleII_stone_page6.png"],
        ["circleII_stone_page6.png"],
        (128,128)]
    
    circleII_tiles = [
    ["C", "circleII_wall", (128,128),None,False,None,None],
    ["L", "circleII_wall-left", (128,128),None,False,None,None],
    ["R", "circleII_wall-right", (128,128),None,False,None,None],
    ["g", "circleII_stone", (128,128),None, False, None,None],
    ]
    
    circleII_layout =[
    "CCCLoRCCC",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "CCLoooRCC",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooLo+oRoo",
    "ooCCCCCoo",
    ]
    
    circleIIa_layout =[
    "CCCLoRCCC",
    "Looo+oooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "CCLoooRCC",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooCCCCCoo",
    ]
    
    circleIIb_layout =[
    "CCCLoRCCC",
    "Looo+oooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "CCLoooRCC",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooCCCCCoo",
    ]
    
    circleIIX_layout =[
    "CCCLoRCCC",
    "Looo+oooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "CCLoooRCC",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooCCCCCoo",
    ]
    
    
    circleII_portal_tiles = [['q', 'circleIII']]
    circleII_portals =[
    "ooooqoooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    ]
    
    circleIIa_portal_tiles = [['q', 'circleIIIax']]
    circleIIa_portals =[
    "ooooqoooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    ]
    
    circleIIb_portal_tiles = [['q', 'circleIIIbx']]
    circleIIb_portals =[
    "ooooqoooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    ]
    
    circleII_ground =[
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "oogggggoo",
    "oogggggoo",
    "oogggggoo",
    "oogggggoo",
    ]
    
    circleII_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    circleII_villagers = [
    ["1",None, False, page1_sprites,  "right", "page1"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["3",None, False, page3_sprites,  "right", "page3"],
    ["4",None, False, page4_sprites,  "right", "page4"],
    ["5",None, False, page5_sprites,  "right", "page5"],
    ["6",None, False, page6_sprites,  "right", "page6"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ["X",None, False, virgil_sprites,  "right", "virgilIIa"],
    ["V",None, False, virgil_sprites,  "right", "virgilIIb"],
    ]
    circleII_enemies_layout =[
    "ooooooooo",
    "ooooooooo",
    "oo4o5o6oo",
    "ooooooooo",
    "oo1o2o3oo",
    "ooooooooR",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooovooo",
    "ooooooooo",
    ]
    
    circleIIa_enemies_layout =[
    "ooooooooo",
    "ooooooooo",
    "oo4o5o6oo",
    "ooooooooo",
    "oo1o2o3oo",
    "ooooooooR",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "oooooXooo",
    "ooooooooo",
    ]
    
    circleIIb_enemies_layout =[
    "ooooooooo",
    "ooooooooo",
    "oo4o5o6oo",
    "ooooooooo",
    "oo1o2o3oo",
    "ooooooooR",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "oooooVooo",
    "ooooooooo",
    ]
    
    
    
    
    
    
    
    
    circleIII_tiles = [
    ["C", "circleIII_wall", (128,128),None,False,None,None],
    ["L", "circleIII_wall-left", (128,128),None,False,None,None],
    ["R", "circleIII_wall-right", (128,128),None,False,None,None],
    ["g", "circleIII_stone", (128,128),None, False, None,None],
    ["E", "hell_cerberus", (394,256),None, False, None,None],
    ]
    
    circleIII_layout =[
    "oooLoRooo",
    "CCCLoRCCC",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "CCLoooRCC",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooLo+oRoo",
    "ooCLoRCoo",
    ]
    
    circleIIIa_layout =[
    "oooLoRooo",
    "CCCLoRCCC",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "Looo+oooR",
    "CCLoooRCC",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooCLoRCoo",
    ]
    
    circleIIIax_layout =[
    "oooLoRooo",
    "CCCLoRCCC",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "CCLoooRCC",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooLo+oRoo",
    "ooCLoRCoo",
    ]
    
    circleIIIbx_layout =[
    "oooLoRooo",
    "CCCLoRCCC",
    "LooooooR",
    "LoooooooR",
    "LoooooooR",
    "LoooooooR",
    "CCLoooRCC",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooLo+oRoo",
    "ooCLoRCoo",
    ]
    
    circleIIIb_layout =[
    "oooLoRooo",
    "CCCLoRCCC",
    "LoooooooR",
    "LoooooooR",
    "Looo+oooR",
    "LoooooooR",
    "CCLoooRCC",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooLoooRoo",
    "ooCLoRCoo",
    ]
    
    circleIII_portal_tiles = [['q', 'cerberus_blocker'], ['p', 'circleIIX']]
    circleIII_portals =[
    "ooooooooo",
    "ooooooooo",
    "oooqqqooo",
    "oooqqqooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "oooopoooo",
    ]
    
    circleIIIa_portal_tiles = [['q', 'cerberus_blocker'], ['p', 'circleIIa']]
    circleIIIa_portals =[
    "ooooooooo",
    "ooooooooo",
    "oooqqqooo",
    "ooqqqqooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "oooopoooo",
    ]
    
    circleIIIb_portal_tiles = [['q', 'circleIV'], ['p', 'circleIIb']]
    circleIIIb_portals =[
    "ooooqoooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "oooopoooo",
    ]
    
    circleIII_ground =[
    "ooogggooo",
    "ggggggggg",
    "gggEooggg",
    "gggoooggg",
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "oogggggoo",
    "oogggggoo",
    "oogggggoo",
    "oogggggoo",
    ]
    
    circleIII_ground_final =[
    "ooogggooo",
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "ggggggggg",
    "oogggggoo",
    "oogggggoo",
    "oogggggoo",
    "oogggggoo",
    ]
    
    circleIII_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    circleIII_villagers = [
    ["1",None, False, page1_sprites,  "right", "page1"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["3",None, False, page3_sprites,  "right", "page3"],
    ["4",None, False, page4_sprites,  "right", "page4"],
    ["5",None, False, page5_sprites,  "right", "page5"],
    ["6",None, False, page6_sprites,  "right", "page6"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ]
    circleIII_enemies_layout =[
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    "ooooooooo",
    ] 
    
    
    
    
    
    # Circle IV
    circleIV_tiles = [
    ["C", "circleIV_wall", (128,128),None,False,None,None],
    ["L", "circleIV_wall-left", (128,128),None,False,None,None],
    ["R", "circleIV_wall-right", (128,128),None,False,None,None],
    ["g", "circleIV_stone", (128,128),None, False, None,None],
    ["E", "plutus_ground", (384,384),None, False, None,None],
    ]
    
    circleIV_layout =[
    "ooooooooEooooooooooo",
    "CCCCCCCCoooCCCCCCCoo",
    "LooooooooooooooooRCC",
    "L+oooooooooooooooooo",
    "LooooooooooooooooRCC",
    "CCCCCCCCCCCCCCCCCCCC",
    ]
    
    circleIVaa_layout =[
    "ooooooooEooooooooooo",
    "CCCCCCCCoooCCCCCCCoo",
    "LooooooooooooooooRCC",
    "Looooooooooooooooo+o",
    "LooooooooooooooooRCC",
    "CCCCCCCCCCCCCCCCCCCC",
    ]

    circleIVtalk_layout =[
    "ooooooooEooooooooooo",
    "CCCCCCCCoooCCCCCCCoo",
    "LooooooooooooooooRCC",
    "Looooooooooooooooo+o",
    "LooooooooooooooooRCC",
    "CCCCCCCCCCCCCCCCCCCC",
    ]
    
    circleIV_portal_tiles = [['q', 'circleVa'], ['p', 'circleIIX']]
    circleIVb_portal_tiles = [['q', 'circleVbb'], ['p', 'circleIIX']]
    circleIVtalk_portal_tiles = [['q', 'circleVtalk'], ['p', 'circleIIX']]
    circleIVfin_portal_tiles = [['q', 'circleVfin'], ['p', 'circleIIX']]
    circleIV_portals =[
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooq",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    
    circleIV_ground =[
    "ooooooooEooooooooooo",
    "ooooooooooooooooggoo",
    "ggggggggoooggggggggo",
    "gggggggggggggggggggg",
    "gggggggggggggggggggo",
    "oooooooooooooooooooo",
    ]
    
    
    circleIV_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    circleIV_villagers = [
    ["P",None, False, plutus_sprites,  "right", "plutus_a"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ]
    
    circleIVb_villagers = [
    ["P",None, False, plutus_sprites,  "right", "plutus_b"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ]
    
    circleIVtalk_villagers = [
    ["P",None, False, plutus_sprites,  "right", "plutus_talk"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ]
    circleIVfin_villagers = [
    ["P",None, False, plutus_sprites,  "right", "plutus_fin"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["v",None, False, virgil_sprites,  "right", "virgilIV"],
    ]
    circleIV_enemies_layout =[
    "ooooooooPooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    circleIVfin_enemies_layout =[
    "ooooooooPooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooovooo",
    "oooooooooooooooooooo",
    ]
    
    
    
    
    
    # Circle V (Styx Pier)
    circleV_tiles = [
    ["C", "circleV_wall", (128,128),None,False,None,None],
    ["L", "circleV_wall-left", (128,128),None,False,None,None],
    ["R", "circleV_wall-right", (128,128),None,False,None,None],
    ["1", "circleV_pier1", (128,128),None, False, None,None],
    ["2", "circleV_pier2", (128,128),None, False, None,None],
    ["3", "circleV_pier3", (128,128),None, False, None,None],
    ["4", "circleV_pier4", (128,128),None, False, None,None],
    ["d", "circleV_dark", (128,128),None, False, None,None],
    ["g", "circleV_stone", (128,128),None, False, None,None],
    ["E", "phlegyas", (384,384),None, False, None,None],
    ]
    
    circleV_layout =[
    "ooooCCLddddddddddddddddddddddEoo",
    "ooooo+oooooooooooooooooooooooooo",
    "ooooCCL4444444444444444444444ooo",
    "oooooooooooooooooooooooooooooooo",
    ]
    
    circleVb_layout =[
    "ooooCCLddddddddddddddddddddddEoo",
    "oooooooooooooooooooooooooooo+ooo",
    "ooooCCL4444444444444444444444ooo",
    "oooooooooooooooooooooooooooooooo",
    ]

    
    circleV_portal_tiles = [['q', 'circleIVaa'],]
    
    circleV_portals =[
    "oooooooooooooooooooooooooooooooo",
    "ooooqooooooooooooooooooooooooooo",
    "oooooooooooooooooooooooooooooooo",
    "oooooooooooooooooooooooooooooooo",
    ]
    
    circleVb_portal_tiles = [['q', 'circleIVb'],]
    circleVtalk_portal_tiles = [['q', 'circleIVtalk'],]
    circleVfin_portal_tiles = [['q', 'circleIVfin'],]
    circleVb_portals =[
    "oooooooooooooooooooooooooooooooo",
    "ooooqooooooooooooooooooooooooooo",
    "oooooooooooooooooooooooooooooooo",
    "oooooooooooooooooooooooooooooooo",
    ]
    
    
    circleV_ground =[
    "dddddddooooooooooooooooooooooddd",
    "ddddgg12222222222222222222223ddd",
    "ddddddd4444444444444444444444ddd",
    "dddddddddddddddddddddddddddddddd",
    ]
    
    
    circleV_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    circleV_villagers = [
    ["H",None, False, phlegyas_sprites,  "right", "phlegyas_a"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ]
    
    circleVtalk_villagers = [
    ["H",None, False, phlegyas_sprites,  "right", "phlegyas_talk"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ]
    circleVfin_villagers = [
    ["H",None, False, phlegyas_sprites,  "right", "phlegyas_fin"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ]
    circleV_enemies_layout =[
    "oooooooooooooooooooooooooooooHoo",
    "ooooqooooooooooooooooooooooooooo",
    "oooooooooooooooooooooooooooooooo",
    "oooooooooooooooooooooooooooooooo",
    ]
    
    
    # Lavender 1
    lavender1_tiles = [
    ["C", "circleV_wall", (128,128),None,False,None,None],
    ["L", "circleV_wall-left", (128,128),None,False,None,None],
    ["R", "circleV_wall-right", (128,128),None,False,None,None],
    ["1", "circleV_pier1", (128,128),None, False, None,None],
    ["2", "circleV_pier2", (128,128),None, False, None,None],
    ["3", "circleV_pier3", (128,128),None, False, None,None],
    ["4", "circleV_pier4", (128,128),None, False, None,None],
    ["d", "circleV_dark", (128,128),None, False, None,None],
    ["g", "circleV_stone", (128,128),None, False, None,None],
    ["A", "lavender_town_green", (576,768),None, False, None,None],
    ]
    
    lavender1_layout =[
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "ooooooooo+oooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    


    
    lavender1_portal_tiles = [['w', 'lavender1'],]
    lavender1_portals =[
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooowwwwwwwooooooo",
    "oooooowooooowooooooo",
    "oooooowooooowooooooo",
    "oooooowoo+oowooooooo",
    "oooooowooooowooooooo",
    "oooooowooooowooooooo",
    "oooooowwwwwwwooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    
    lavender1_ground =[
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    ]
    
    
    lavender1_enemies = [
    ["H", (512,512), True, lovecraft_sprites, "down", "demon_catch", ari_battle],
    ]
    lavender1_villagers = [
    ["R",None, False, lovecraft_sprites,  "right", "lovecraft_catch"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ]
    lavender1_enemies_layout =[
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooRoooooooooo",
    "oooooooooooooooooooo",
    "ooooooooo+oooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    
    # Lavender 2
    lavender2_tiles = [
    ["A", "lavender_town_green", (576,768),None, False, None,None],
    ]
    
    lavender2_layout =[
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "ooooooooo+oooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    


    
    lavender2_portal_tiles = [['w', 'lavender2'],]
    lavender2_portals =[
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "ooowwwwwwwwwwwwwwwoo",
    "ooowooooooooooooowoo",
    "ooowooooooooooooowoo",
    "ooowooooooooooooowoo",
    "ooowooooooooooooowoo",
    "ooowooooooooooooowoo",
    "ooowooooooooooooowoo",
    "ooowooooooooooooowoo",
    "ooowooooooooooooowoo",
    "ooowoooooooooooooowo",
    "oowwoooooooooooooowo",
    "oowooooooooooooooowo",
    "oowooooooooooooooowo",
    "oowooooooooooooooowo",
    "oowooooooooooooooowo",
    "oowwwwwwwwwwwwwwwwwo",
    "oooooooooooooooooooo",
    ]
    
    
    lavender2_ground =[
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAA",
    ]
    
    
    lavender2_enemies = [
    ["H", (512,512), True, lovecraft_sprites, "down", "demon_catch", ari_battle],
    ]
    lavender2_villagers = [
    ["R",None, False, victim_sprites,  "right", "victim_catch"],
    ["2",None, False, page2_sprites,  "right", "page2"],
    ["v",None, False, virgil_sprites,  "right", "virgilII1"],
    ]
    lavender2_enemies_layout =[
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooRoooooooooooooo",
    "oooooooooooooooRoooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "ooooooooo+oooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "ooooooRooooooooooooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    "ooooooooooooooooRooo",
    "oooooooooooooooooooo",
    "oooooooooooooooooooo",
    ]
    
    
    
    
    
    
    
    
    
    
    #TILESETS
    null_tiles = [
    ["N", "null_tile", (128,128),None,False,None,None],
    ]
    
    null_layout =[
    "+",
    ]
    
    null_portal_tiles = [['p', 'deeemon']]
    null_portals =[
    "p",
    ]
    
    null_ground =[
    "N",
    ]
    
    null_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null_villagers = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null_enemies_layout =[
    "o",
    ]
    
    
    #null_2
    null2_tiles = [
    ["N", "null_tile", (128,128),None,False,None,None],
    ]
    
    null2_layout =[
    "+",
    ]
    
    null2_portal_tiles = [['p', 'lovecraft_caught']]
    null2_portals =[
    "p",
    ]
    
    null2_ground =[
    "N",
    ]
    
    null2_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null2_villagers = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null2_enemies_layout =[
    "o",
    ]
    
    
    
    #null_3
    null3_tiles = [
    ["N", "null_tile", (128,128),None,False,None,None],
    ]
    
    null3_layout =[
    "+",
    ]
    
    null3_portal_tiles = [['p', 'victim_intro']]
    null3_portals =[
    "p",
    ]
    
    null3_ground =[
    "N",
    ]
    
    null3_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null3_villagers = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null3_enemies_layout =[
    "o",
    ] 
    
    #null_4
    null4_tiles = [
    ["N", "null_tile", (128,128),None,False,None,None],
    ]
    
    null4_layout =[
    "+",
    ]
    
    null4_portal_tiles = [['p', 'plutus_battle']]
    null4_portals =[
    "p",
    ]
    
    null4_ground =[
    "N",
    ]
    
    null4_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null4_villagers = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null4_enemies_layout =[
    "o",
    ] 
    #null_5
    null5_tiles = [
    ["N", "null_tile", (128,128),None,False,None,None],
    ]
    
    null5_layout =[
    "+",
    ]
    
    null5_portal_tiles = [['p', 'circleVIb']]
    null5_portals =[
    "p",
    ]
    
    null5_ground =[
    "N",
    ]
    
    null5_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null5_villagers = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null5_enemies_layout =[
    "o",
    ] 
    
    #null_6
    null6_tiles = [
    ["N", "null_tile", (128,128),None,False,None,None],
    ]
    
    null6_layout =[
    "+",
    ]
    
    null6_portal_tiles = [['p', 'dis_room']]
    null6_portals =[
    "p",
    ]
    
    null6_ground =[
    "N",
    ]
    
    null6_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null6_villagers = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null6_enemies_layout =[
    "o",
    ] 
      
    #null_7
    null7_tiles = [
    ["N", "null_tile", (128,128),None,False,None,None],
    ]
    
    null7_layout =[
    "+",
    ]
    
    null7_portal_tiles = [['p', 'bee_battle']]
    null7_portals =[
    "p",
    ]
    
    null7_ground =[
    "N",
    ]
    
    null7_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null7_villagers = [
    ["a", (512,512), True, demon01_sprites, "down", "demon_catch", ari_battle],
    ]
    null7_enemies_layout =[
    "o",
    ]   
      
    #signifier, base name, building size, roof size, has roof, goToLabel, actionLabel (used for descriptions)
    moordell_tiles = [
    ["1","bee_house-1", (256,216), None,False,None,"building_quitelocked"],
    ["2","bee_house-2", (256,216), None, False,None,"building_verylocked"],
    ["3","bee_house-3", (256,216), None,False,None,"building_extremelylocked"],
    ["5","bee_house-3", (256,216), None,False,None,"building_locked"],
    ["6","bee_house-3", (256,216), None,False,None,"building_unlocked"],
    ["*","bee_inn", (342,216),None,False, "inn","inn_desc"],
    ["h","bee_inn", (342,216),None,False, "inn2","inn_desc"],
    ["n", "cute_buildings/wall", (128,128),None,False,None,None],
    ["e", "cute_buildings/wall", (128,128),None,False,None,None],
    ["w", "cute_buildings/wall", (128,128),None,False,None,None],
    ["s", "cute_buildings/wall", (128,128),None, False,None,None],
    ["p", "dirt", (128,128),None, False, None,None],
    ["g", "grass", (128,128),None, False, None,None],
    ["H", "path_horz", (128,128),None, False, None,None],
    ["V", "path_vert", (128,128),None, False, None,None],
    ["J", "path_junc", (128,128),None, False, None,None],
    ["C", "wall", (128,128),None,False,None,None],
    ["L", "wall-left", (128,128),None,False,None,None],
    ["R", "wall-right", (128,128),None,False,None,None],
    ]
    
    moordell2_tiles = [
    ["1","bee_house-1", (256,216), None,False,None,"building_quitelocked"],
    ["2","bee_house-2", (256,216), None, False,None,"building_verylocked"],
    ["3","bee_house-3", (256,216), None,False,None,"building_extremelylocked"],
    ["5","bee_house-3", (256,216), None,False,None,"building_locked"],
    ["6","bee_house-3", (256,216), None,False,None,"building_unlocked"],
    ["*","bee_inn", (342,216),None,False, "inn","inn_desc"],
    ["h","bee_inn", (342,216),None,False, "inn2","inn_desc"],
    ["n", "cute_buildings/wall", (128,128),None,False,None,None],
    ["e", "cute_buildings/wall", (128,128),None,False,None,None],
    ["w", "cute_buildings/wall", (128,128),None,False,None,None],
    ["s", "cute_buildings/wall", (128,128),None, False,None,None],
    ["p", "dirt", (128,128),None, False, None,None],
    ["g", "grass", (128,128),None, False, None,None],
    ["H", "path_horz", (128,128),None, False, None,None],
    ["V", "path_vert", (128,128),None, False, None,None],
    ["J", "path_junc", (128,128),None, False, None,None],
    ["C", "wall", (128,128),None,False,None,None],
    ["L", "wall-left", (128,128),None,False,None,None],
    ["R", "wall-right", (128,128),None,False,None,None],
    ]
    
    #signifier, range, roaming,  sprite set, facing, associated battle label, associated battle
    moordell_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "ari_caught", ari_battle],
    ]
    
    moordell2_enemies = [
    ["a", (512,512), True, demon01_sprites, "down", "ari_caught", ari_battle],
    ]
    
    #signifier, range, roaming,  sprite set, facing, conversation label
    moordell_villagers = [
    ["9", (256,256), True, villager_sprites, "down", "talky_label"], #example of roaming NPC
    ["6", (256,256), True, villager_sprites, "down", "talky4"],
    ["4",None, False, villager_sprites,  "down", "talky3"],
    ["b",None, False, villager_sprites,  "down", "talky2"], #example of static NPC
    ["v",None, False, virgil_sprites,  "right", "virgilVI"],
    ]
    moordell2_villagers = [
    ["9", (256,256), True, villager_sprites, "down", "talky_label"], #example of roaming NPC
    ["6", (256,256), True, villager_sprites, "down", "talky4"],
    ["4",None, False, villager_sprites,  "down", "talky5"],
    ["b",None, False, villager_sprites,  "down", "talky2"], #example of static NPC
    ["v",None, False, virgil_sprites,  "right", "virgilVIb"],
    ]
    
    #[signifier, goToLabel]
    moordell_portal_tiles = [['p', 'leave_city']]
    moordell2_portal_tiles = [['p', 'leave_city']]
    
    
    #MAP LAYOUTS
    #these maps should align for ease of use. 
    #If they don't look square, switch to a monospace font like consolas!   
    
    moordell_layout =[
    "CCCCCCCCCCCCCCC",
    "L3oo*ooo2oo1ooR",
    "LoooooooooooooR",
    "Loooooo+ooooooR",
    "L3oooooo1oooooR",
    "LoooooooooooooR",
    "LoooooooooooooR",
    "L2o3ooooo1oo5oR",
    "LoooooooooooooR",
    "LoooooooooooooR",
    "L3ooo1o3o2oo1oR",
    "LoooooooooooooR",
    "LoooooooooooooR",
    "L1o2o2ooo3o1ooR",
    "LoooooooooooooR",
    "LoooooooooooooR",
    "CCCCCCCCCCCCCCC",
    ]
    
    moordell2_layout =[
    "CCCCCCCCCCCCCCC",
    "L3oohooo2oo1ooR",
    "LoooooooooooooR",
    "LoooooooooooooR",
    "L3oooooo1oooooR",
    "LoooooooooooooR",
    "LoooooooooooooR",
    "L2o3ooooo1oo6oR",
    "LoooooooooooooR",
    "LoooooooooooooR",
    "L3ooo1o3o2oo1oR",
    "LoooooooooooooR",
    "LoooooooooooooR",
    "L1o2o2ooo3o1ooR",
    "Loooooooooooo+R",
    "LoooooooooooooR",
    "CCCCCCCCCCCCCCC",
    ]
  
    moordell_portals =[
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    ]
    
    moordell2_portals =[
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    ]
    
    
    moordell_ground =[
    "gggggggVggggggg",
    "gggggggVggggggg",
    "gggggggVggggggg",
    "HHHHHHHJHHHHHHH",
    "gggggggVggggggg",
    "gggggggVggggggg",
    "HHHHHHHJHHHHHHH",
    "gggggggVggggggg",
    "gggggggVggggggg",
    "HHHHHHHJHHHHHJH",
    "gggggggggggggVg",
    "gggggggggggggVg",
    "gggggggggggggVg",
    "HHHHHHHHHHHHHJH",
    "ggggggggggggggg",
    "ggggggggggggggg",
    "ggggggggggggggg",
    ]
    
    moordell2_ground =[
    "gggggggVggggggg",
    "gggggggVggggggg",
    "gggggggVggggggg",
    "HHHHHHHJHHHHHHH",
    "gggggggVggggggg",
    "gggggggVggggggg",
    "HHHHHHHJHHHHHHH",
    "gggggggVggggggg",
    "gggggggVggggggg",
    "HHHHHHHJHHHHHJH",
    "gggggggggggggVg",
    "gggggggggggggVg",
    "gggggggggggggVg",
    "HHHHHHHHHHHHHJH",
    "ggggggggggggggg",
    "ggggggggggggggg",
    "ggggggggggggggg",
    ]
  
    moordell_enemies_layout =[
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "oooooooovoooooo",
    "ooooooooooooooo",
    "ooooo9ooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooboooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooo6ooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooo4o",
    "ooooooooooooooo",
    ]

    moordell2_enemies_layout =[
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "oooooooovoooooo",
    "ooooooooooooooo",
    "ooooo9ooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooboooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooo6ooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooooo",
    "ooooooooooooo4o",
    "ooooooooooooooo",
    ]
