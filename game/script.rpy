# Aqui está o código combinado com as substituições feitas:
#filme
init:
    image movie = Movie(size=(400, 300), xalign=0.5, yalign=0.5)

define e = Character('josilvan', color="#ffffff")
define b = Character('pedro')
define g = Character('guga')
define p = Character('pessoas morrendo')

define r = Character('Josilvan', color="#CD0000")
define w = Character('Guga', color="#B5B5B5")

#background
image comeso = "rpzeocoiso.jpg"
image quarto = "oqrolou.jpg"
image black = "oqrolou.jpg"  # Adicionei uma imagem preta para a cena de batalha
image puto = "josilvanputo.jpg"
image josilvanemo= "josilvanvegeta.png"
image chuva="chuva.jpg"
image preto="telapreta.jpg"
image chuvin="chuvanime.jpg"
image fim="deladofim.png"
image quart="chuvaquart.jpg"
image dia="hospital1.png"
image boteco="boteco.jpg"
image caminhada="caminhada.jpg"
image fim="hellscape1.png"
image dark="josilvandark.png"
image mund="fim do mundo.jpg"
image davi="pedroedavi.jpg"
image fogoo="fogoo.png"
image quebra1="quebra1.png"
image quebra2="quebra2.png"
image quebra3="quebra3.png"
image quebra4="quebra4.png"
image quebra5="quebra5.png"
image pont0="pont0.png"
image pont1="pont1.png"
image pont2="pont2.png"
image pont3="pont3.png"
image cortzin1="cortizin1.png"
image cortzin2="cortizin2.png"
image cortzin3="cortizin3.png"
image cortzin4="cortizin4.png"
image cortzin5="cortizin5.png"
image cortzin6="cortizin6.png"
image cortzin7="cortizin7.png"
image cortzin8="cortizin8.png"
image cort1="g1.png"
image cort2="g2.png"
image cort3="g3.png"
image caixa1="sangue1.png"
image caixa2="sangue2.png"
image caixao="fpedro.png"
image fstofo="fasltfo.jpg"
image fim1="sacr1.png"
image fim2="sacr2.png"
image fim3="sacr3.png"
image fim4="sacr4.png"
image bar="bardoze.png"
image dom="expansaopedro.png"
image dom2="expansaopedro2.png"
image dom3="expansaopedro3.png"
image dom4="expansaopedro4.png"
image dom5="expansaopedro5.png"
image dom6="expansaopedro6.png"
image dom7="expansaopedro7.png"
image dom8="expansaopedro8.png"
image cara="caraodrag.png"
image golpe1="golpe1.png"
image golpe2="golpe2.png"
image golpe3="golpe3.png"
image golpe4="golpe4.png"
image golpe5="golpe5.png"
image rugido1="rugido0.png"
image rugido2="rugido.png"
image caixa="josilvan caixa.png"
image luz1="luzdofim0.png"
image luz2="luzdofim.png"
image ceuemo="ceuemo.png"
image josiceu="josilvanoceu.png"




#imagem dos bonecos
image copstof="astolfocorpo.png"
image astolfoemo="astolfodark.png"
image josilvan = "josilvan.png"
image astolfo = "astolfo.png"
image putocalvo = "josilvanputocalvo.png"
image gugare = "guga.png"
image gugasoled="gugasolado.png"
image blackcalvo="blackcalvo.png"
image josidark="blekcalvo.png"
image josilfight="josilfight.png"

screen simple_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Josilvan" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value red_hood_hp
                    range red_hood_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                null width 5
                text "[red_hood_hp] / [red_hood_max_hp]" size 16

    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Guga" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value wolf_hp
                    range wolf_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                null width 5
                text "[wolf_hp] / [wolf_max_hp]" size 16

    text "Josilvan vs. Guga" xalign 0.5 yalign 0.05 size 30

label start:
    camera: 
        perspective True
    scene comeso with fade    

    play music "pisadinha.mp3"
    
    show josilvan:
        zoom 1.3 
        subpixel True ypos 589 


    with dissolve
    e "vamo beber"
    show astolfo at right 
    with dissolve
    b "num vo nao"
    e "rpz venha beber, te faço um negocin"
    b "num vo n"
    
    
    menu:
        "num vo":
            jump numir
        "Eu vo":
            jump euvo

label numir:
    e "rpz n diga isso"
    b "num quero"
    scene puto with dissolve

    "josilvan chega para tomar uma sozinho, movido pelo ódio e depressão pela rejeição de pedro, josilvan queima o barzin de guga"

    show putocalvo at truecenter with dissolve
    e "pai ta emo"

    stop music
    play music"GUGABOSS.mp3"


    show putocalvo at topleft with dissolve
    
    "vendo a destruição causada em seu estabelecimento, guga, guerreiro antigo que agora descansava enquanto cuidava de sua filha, desperta de seu sono pós latinha de monster e decide confrontar josilvan"

    show gugare at right with dissolve
    g "josilvan meu rei"

    jump battle_game_1

label euvo:
    e "umbora"
    b "lerigo"
    
    scene quarto with fade
    "chegando na praia, josilvan olha para pedro e faz uma pergunta interessante..."
    show josilvan at right with dissolve
    e "pedro eu posso passar tua marcha?"
    show astolfo at left with dissolve
    b "pode meu amor, meu lindo josilvan"
    return

label battle_game_1:
    $ wolf_max_hp = 30
    $ red_hood_max_hp = 50
    $ wolf_hp = wolf_max_hp
    $ red_hood_hp = red_hood_max_hp
    $ cookies_left = 13
    
label battle_1_loop:
    show screen simple_stats_screen
    
    while (wolf_hp > 0) and (red_hood_hp > 0):
        menu:
            "Atack!":
                $ wolf_hp -= 8
                r "BORA BILL"
                
            "dar monster pro guga (got [cookies_left] cookies left)" if cookies_left > 0:
                $ wolf_hp = min(wolf_hp+5, wolf_max_hp)
                $ cookies_left -= 1
                r "Mmm, tasty... (restore 5hp)"
        
        $ wolf_damage = renpy.random.randint(1, 6)
        $ red_hood_hp -= wolf_damage
        w "LA ELE {i}SE MATE MEU REI{/i} ( [wolf_damage] de dano)"

    hide screen simple_stats_screen
    
    if wolf_hp <= 0:
        if red_hood_hp <= 0:
            "Double KO"
        else:
            play music "josilvantriste.mp3"
            scene puto with dissolve
            "guga olhava com odio para josilvan enquanto falava"
            show gugasoled:
                subpixel True pos (0, -236) zoom 6.24 
            with dissolve
            g"eu ja não te reconheço mais jolsilvan, vc se tornou possesivo"
            g"eu te considerava um amigo..." 
            g"mas vc josilvan"
            g"vc destruiu nossa amizade"
            g"Eu irei te dar um ultimo aviso"
            g"Se continuar assim, pedro nunca irá te amar josilvan..."

            "Ao terminar a frase, guga desiste de seu antigo amigo e vai embora com corpo e alma feridos"
            hide gugasoled with dissolve
            show josilvanemo at truecenter
            with dissolve


            "Josilvan sai vitorioso, utilizando o poder de bill e fi do bill para sobrepujar guga, ele olha a destruição que causou e se questiona:"

        
            e "eu sou forte por ser josilvan, ou sou josilvan por ser forte?"
           
    else:
        w "Om-nom-nom-nom {i}*wolf ate you all up*{/i} (along with the basket, of course...)"
    
    jump battle_1_ending

label battle_1_ending:
    scene chuvin with dissolve
    "josilvan caminhava sem rumo pela cidade enquanto chovia"
    "ele para e fecha os olhos"

    scene preto with fade
    menu decisao_foda:
        e"Pedro não quis tomar uma comigo" 
        "EU SO QUERIA TOMAR UMA":
            jump refletir
       
    with dissolve
    
label refletir:

    play music"tristeemo.mp3"
    
    scene chuva:
        xzoom 1.21 yzoom 1.14 zoom 1.04 
    with fade        

    "Cansado, abalado e abandonado, josilvan caminhava para casa"
    "Atormetado pelas palavras de guga, ele se questiona:,"
    e"se não posso ter pedro, como posso viver? Para oque eu vivo?"
    e"se tenho que viver sem pedro, eu não viverei..."
    "tomado por um sentimento de furia e armagura, josilvan ja estava em um caminho sem volta"


scene preto:
    xzoom 1.21 yzoom 1.14 zoom 1.04
with dissolve
play music"galo.mp3"
menu final_ep1:
    "JOGO FODA":
        jump part2


label part2:
    play music "narutoost.mp3"
    scene quart:
        subpixel True zoom 0.53
    with fade
    "josilvan tomado pela depressão chega em casa"
    "revoltado com seu estado atual, josilvan decide se voltar contra o mundo"
    "não foi uma escolha facil, josilvan iria seguir um rumo solitario e dificil"
    "ele decide dormir"
    scene preto with fade
    "josilvan sonha tomando uma com pedro"
    scene boteco:
        subpixel True xzoom 1.13 yzoom 0.87 zoom 0.85
    with fade
    "josilvan, pedro e guga em seus dias felizes"
    scene dia:
        subpixel True xzoom 1.04 yzoom 0.78 zoom 2.31
    with fade
    "josilvan acorda..."
    e"talvez eu deva dar uma caminhada"
    "josilvan resolve fazer sua caminhada diaria"
    scene caminhada with fade
    "josilvan andava sem rumo perdido em seus pensamentos"
    e"..."
    "ate que.."
    "josilvan tomou uma decisão:"
    show blackcalvo:
        subpixel True pos (-86, 0) xzoom 6.22 yzoom 6.5
    with dissolve
    "SE PREPARE PEDRO!"
    


menu caminhada:
    e"trarei o fim!!"
    "{color=#FF0000}QUE COMECE O FIM{/color}":  
        jump x1_pedro

label x1_pedro:
    play music "trta.mp3"
    scene dark:
        subpixel True xzoom 2.36 yzoom 2.4 zoom 0.49
    with fade
    "josilvan trouxe o caos ao mundo, destruiu lares e familias"
    "se ele não pode ter pedro, o mundo tambem não"
    "e então ele começou"
    scene pont0:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.29
    with fade
    pause 0.4
    scene pont1:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.29
    pause 0.4
    scene pont2:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.29
    pause 0.4
    scene pont3:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.29
    pause 0.4
   

    scene mund with fade
    "josilvan ja não tem mais volta"
    "ele está perdido"
    "tudo oq ele queria era tomar uma"
    "ele continuou destruindo tudo"
    p"AAAAAAAAAAAAAAAAAAA"
    p"ALGUEM PARE AQUELE CALV-"
    "josilvan naquele ponto ja considerava a humanidade um erro"


    scene fim:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.39
    with dissolve

    show josidark
    with dissolve

    play sound"risadaemo.mp3"
    e"heheheheheh"

    "orgulhoso de sua destruição, josilvan estava feliz"
    "mas ele sentia que algo faltava"
    "nesse momento ja era obvio"
    "ele deveria concluir sua vingança contra aquele que o deixou de lado"
    "enquanto ria josilvan continuava sua busca"


    e"pedro..."

    play sound"risadaemo.mp3"
    e"heheheheheh"



    scene fogoo:
        subpixel True xpos 0 xzoom 6.25 yzoom 4.69 zoom 0.24
    with fade
    
    "apenas a destruição seguia josilvan"
    "mesmo o barzin de seu zé foi reduzido a cinzas"

    
    
    stop sound
    menu:
        "o outro lado":
            jump pedro_e_davi

label pedro_e_davi:
    scene fogoo:
        subpixel True xpos 0 xzoom 6.25 yzoom 4.69 zoom 0.24
    play music "uta.mp3"
    with dissolve
    "pedro estava aflito após saber o que josilvan estava causando"
    "ele se questionava se deveria ter ido tomar uma"
    "mas pedro não queria iludir josilvan e dar chances de algo que nunca foi real"
    "porém pedro sabia, ele teria que parar josilvan"
    "ele era o único que restava para josilvan"

    show astolfoemo:
        subpixel True xzoom 3.43 yzoom 3.41
    with dissolve
    "O que Josilvan está fazendo?"
    "Eu não queria que nada disso estivesse acontecendo"
    "Por que você teve que ficar assim, Josilvan? Você era tão legal e amável"

    scene fogoo:
        subpixel True xpos 0 xzoom 6.25 yzoom 4.69 zoom 0.24
    with fade 

    show josidark
    
    show josidark at left with move
    
    "..."

    show copstof
    show copstof at right with move

    "..."

    scene preto

    "Em silêncio, uma batalha triste de dois amigos começava"
    play music "next.mp3"

    scene cortzin1:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.24
    with fade
    pause 0.4
    scene cortzin2:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.24
    pause 0.4
    scene cortzin3:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.24
    pause 0.4
    scene cortzin4:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.24
    pause 0.4
    scene cortzin5:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.24
    pause 0.4
    scene cortzin6:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.24
    pause 0.4
    scene cortzin7:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.24
    pause 0.4
    scene cortzin8:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.24
    pause 0.4


scene preto 
with dissolve
"pedro ja não conseguia suportar o poder de josilvan"
"ele se culpava por não ir tomar uma"
"e a batalha continuou"

scene cort1:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.30
with fade
pause 0.4
scene cort2:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.30
pause 0.4
scene cort3:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.30
pause 0.4

scene caixa2:
    subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.24
pause 1

scene caixao:
    subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.30
pause 0.4


label fpedro:

scene fstofo:
    subpixel True pos (0, 0) xzoom 2.36 yzoom 2.44 zoom 0.64 
with dissolve
"pedro estava ferido e cansado"
"ele sabia que só tinha uma forma de derrotar josilvan"

b"..."

scene preto with fade

"pedro decidiu se sacrificar para parar josilvan"
"ele não poderia amar josilvan, muito menos tomar uma, mas de alguma forma, pedro queria poder fazer algo por seu querido amigo"
"ele concentra toda sua energia em sua mão"
"e antes que josilvan pudesse reagir, pedro começa seu ultimo golpe desesperado"


scene fim1:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.30
with fade
pause 0.4
scene fim2:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.30
pause 0.4
scene fim3:
        subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.30
pause 0.4

scene bar:
    subpixel True xpos 0 xzoom 6.18 yzoom 4.63 zoom 0.30
with dissolve
show astolfoemo:
        subpixel True xzoom 3.43 yzoom 3.41

b"expansão de domínio"
show fim4:
    subpixel True pos (-0.16, 119)
with dissolve
    
b"PEDRO COMBOS MAMADA 2"

play music "dominio.mp3"
scene dom3:
    subpixel True  xzoom 2.01 yzoom 1.17 zoom 0.75
        
with fade
pause 1
scene dom4:
    subpixel True  xzoom 2.01 yzoom 1.17 zoom 0.75
        
pause 1
scene dom5:
    subpixel True xzoom 1.21 yzoom 1.21
    
pause 1

scene dom6:
    subpixel True xzoom 1.21 yzoom 1.21
        
pause 1

scene dom7:
    subpixel True xzoom 1.21 yzoom 1.21
        
pause 1

scene dom8:
    subpixel True xzoom 2.55 yzoom 1.45 zoom 0.47 
        
pause 1


scene cara:
    subpixel True xzoom 1.21 yzoom 1.24
with fade


show josilfight with dissolve

pause 2.0


"pedro deu sua vida em um ultimo golpe desesperado"
"esse dragão representava seu ultimo suspiro para impedir josilvan"
"todo o egoismo de josilvan para tomar uma com pedro, resultou na perca de seu grande amor, mas josilvan ja estava perdido para perceber..."
"mas nada disso importava mais..."
"josilvan estava sozinho"
"seu amor pedro, seu amigo guga, todos ja o haviam deixado para trás"
"independente do resultado desta triste noite, josilvan ja havia perdido..."
"e assim, com o rugido daquele ser majestoso e poderoso, o ultimo combate de josilvan começou"


scene rugido1:
    subpixel True xzoom 2.70 yzoom 1.45 zoom 0.47
pause 0.3

scene rugido2:
    subpixel True xzoom 2.70 yzoom 1.45 zoom 0.47


"foi um rugido estrondoso e poderoso, carregando a tristeza de pedro"
"...o dragão desafiava josilvan"


scene golpe2:
    subpixel True xzoom 1.5 yzoom 1.14
with fade
"com um breve movimento, a besta carmesim começa a absorver toda a energia ao seu redor"
"algo grandioso estava por acontecer"

scene golpe3:
    subpixel True xzoom 1.5 yzoom 1.14
pause 0.4

scene golpe1:
    subpixel True yzoom 0.68 xzoom 1.21  
pause 0.2
with dissolve
scene golpe4:
    subpixel True yzoom 0.68 xzoom 1.21    
pause 1

scene golpe5:
    subpixel True xzoom 1.21 yzoom 1.21    
"o dragão liberou uma poderosa luz, e tudo que estava proximo começou a ser destruido"
"josilvan tentou resistir"
"mas ele não tinha notado uma coisa importante"
"josilvan não tinha tomado uma, ele estava fraco e não suportou todo aquele poder"
"e então ali estava...O FIM de uma historia triste sobre um amor impossivel, de um jovem que queria poder tomar uma, mas por egoismo acabou perdendo tudo, essa foi a historia de josilvan..."


play music "maxim.mp3"
scene josiceu:
    subpixel True xzoom 1.5 yzoom 1.14
with fade
"um rapido raio de luz cobriu o céu"

"nem josilvan, nem pedro estava mais naquele mundo"


scene ceuemo:
    subpixel True xzoom 1.5 yzoom 1.13
with fade
"..."


menu finalsera:
    e"vou realmente ficar sem tomar uma?"
    "se recusar a não tomar uma":
        jump bronyadiva
    "ficar sem tomar uma":
        jump galofoda
    










label galofoda:
play music "galo.mp3"
"LARGUE A CACHAÇA JOSILVAN"
return

label bronyadiva:
scene preto     #continua aqui grazi

scene luz1:
    subpixel True xzoom 1.52 yzoom 1.14
"josilvan acorda em um local escuro"
"tudo oq ele via era um ponto brilhante ao fundo de uma imensidão de solidão"
scene luz2:
    subpixel True xzoom 1.52 yzoom 1.14
"mas ela parecia ficar cada vez mais fraca"
"seria esse realmente o fim de josilvan?"
scene preto
"dasdaasd"


"enquanto a vista de josilvan escurecia, ele vizualizou uma linda calvice..."   #top10ganchosfodas
scene preto #pode alterar a partir daqui, ou antes, toda a label bronyadiva é sua, fiz só um exemplo de gancho, mas pode mudar como quiser
"........."

return 