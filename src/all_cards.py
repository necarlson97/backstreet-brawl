from abc import ABC
from src.card import Card

"""
Below, all card types are defined in separate categories, based loosely
on what they are 'trying to do'
"""
class Strike(Card, ABC):
    # hit them to hurt them
    # TODO want to have a good mix of punches/kicks
    pass
class KnuckleStrike(Strike):
    your_requirements = [
        "smack a hand into them anywhere"
    ]
    your_effects = {
        "focus": +1,
    }
    their_effects = {
        "senses": +1,
        "blood": -1,
    }
    flavor_text = (
        '"Simplicity is the key to brilliance." ~ Bruce Lee'
    )
class SharpJab(Strike):
    your_requirements = [
        "smack a fist into them anywhere"
    ]
    your_effects = {
        "focus": +1,
    }
    their_effects = {
        "senses": +1,
        "pain tolerance": -1,
    }
    flavor_text = (
        '"I fight because I can’t sing, I can’t dance,\n'
        'and it beats working all day.\n'
        'Now ask me a question that doesn’t sound\n'
        'so fucking stupid." ~ Phil Baroni'
    )
class BloodyNose(Strike):
    your_requirements = [
        "smash a fist into their face"
    ]
    your_effects = {
        "focus": -1,
        "rage": +1,
    }
    their_effects = {
        "blood": -1,
        "oxygen": -1,
        "pain tolerance": -1,
    }
    flavor_text = (
        '"It\'s like someone jammed an electric light bulb in your face,\n'
        'and busted it. I thought half my head was blowed off..."\n'
        '~ James J Braddock'
    )
class Haymaker(Strike):
    your_requirements = [
        "smash a fist into them anywhere"
    ]
    your_effects = {
    }
    their_effects = {
        "blood": -1,
        "pain tolerance": -1,
    }
    flavor_text = (
        '"Sure the fight was fixed. I fixed it with a right hand."\n'
        '~ George Foreman'
    )
class CheekSlap(Strike):
    your_requirements = [
        "smack a flat palm into their face"
    ]
    their_effects = {
        "senses": +1,
        "rage": -2,
        "pain tolerance": -1,
    }
    flavor_text = (
        '"I don\'t see why you want me to be a gentleman\n'
        '- we\'re fucking fighting anyway." ~ Mike Tyson'
    )
class Knifehand(Strike):
    your_requirements = [
        "smack a flat palm into their neck"
    ]
    your_effects = {
        "pain tolerance": -1,
        "focus": -1,
        "dignity": +1,
    }
    their_effects = {
        "oxygen": -2,
        "focus": -1,
        "senses": -1,
    }
    flavor_text = (
        '"Remember... you are expressing the technique,\n'
        'not doing the technique" ~ Bruce Lee'
    )
class Hammerfist(Strike):
    your_requirements = [
        "smack a fist into their head"
    ]
    their_requirements = [
        "are sitting or prone"
    ]
    your_effects = {
        "blood": -1,
        "rage": +1,
    }
    their_effects = {
        "blood": -2,
        "senses": -2,
    }
    flavor_text = (
        '"Before you embark on a journey of revenge, dig two graves."\n'
        '~ Confucius'
    )
class ThroatPunch(Strike):
    your_requirements = [
        "smash a fist into their neck"
    ]
    your_effects = {
        "focus": -1,
        "rage": +1,
    }
    their_effects = {
        "oxygen": -2,
        "senses": -2,
    }
    flavor_text = (
        '"Earnie Shavers could punch you in the neck and break your ankle." '
        '~ "Tex" Cobb'
    )

class Uppercut(Strike):
    your_requirements = [
        "smack a fist into their head",
        "have your elbow below that fist"
    ]
    your_effects = {
        "stamina": -1,
    }
    their_effects = {
        "pain tolerance": -1,
        "senses": -1,
        "focus": -1,
    }
    flavor_text = (
        '"Strength is born from the struggle, not the victory."\n'
        '~ Arnold Schwarzenegger'
    )
class SolidHook(Strike):
    your_requirements = [
        "smack a fist into them anywhere",
        "have your elbow on-level with that fist"
    ]
    your_effects = {
    }
    their_effects = {
        "pain tolerance": -1,
        "blood": -1,
    }
    flavor_text = (
        '"We are what we repeatedly do. '
        'Excellence then, is not an act, but a habit" ~ Aristotle'
    )
class Superman(Strike):
    your_requirements = [
        "are airborne",
        "smack a fist into them anywhere",
        "have at least one limb extended behind you",
    ]
    your_effects = {
        "focus": +1,
    }
    their_effects = {
        "pain tolerance": -1,
        "blood": -1,
    }
    flavor_text = (
        '"Don\'t fear failure. — Not failure, but low aim, is the crime. '
        'In great attempts, it is glorious even to fail." ~ Bruce Lee'
    )
class ClinchPummel(Strike):
    your_requirements = [
        "have a grasp hand touching their head, neck, or back of their torso",
        "smack the other hand into their head or torso",
    ]
    your_effects = {
        "pain tolerance": +1,
    }
    their_effects = {
        "pain tolerance": -1,
        "blood": -1,
        "oxygen": -1,
    }
    flavor_text = (
        '"You have two hands like me. Everything is possible.\n'
        'Go. Go. And take it." ~ Yoel Romero'
    )
# Kicks
class FootStrike(Strike):
    your_requirements = [
        "smack a foot into them anywhere"
    ]
    your_effects = {
        "focus": +1,
    }
    their_effects = {
        "senses": +1,
        "pain tolerance": -1,
    }
    flavor_text = (
        '"Fear not who has practiced 10,000 kicks once,\n'
        'but who has practiced one kick 10,000 times."\n~ Bruce Lee'
    )
class CurbStomp(Strike):
    your_requirements = [
        "smack a foot into their head"
    ]
    their_requirements = [
        "are prone"
    ]
    your_effects = {
        "dignity": -1,
        "rage": +1,
    }
    their_effects = {
        "blood": -1,
        "senses": -2,
        "pain tolerance": -1,
    }
    flavor_text = (
        '''"I don't just end fights; I end careers." ~ Axel Vex*'''
    )
class GutKick(Strike):
    your_requirements = [
        "smack a foot into their torso"
    ]
    their_requirements = [
        "are sitting or prone"
    ]
    your_effects = {
        "rage": +2,
    }
    their_effects = {
        "oxygen": -2,
        "pain tolerance": -1,
        "dignity": +1,
    }
    flavor_text = (
        '"Right leg hospital. Left leg cemetary." ~ Cro Cop'
    )
class Gastrizein(Strike):
    your_requirements = [
        "smack a foot into their torso"
    ]
    their_requirements = [
        "are standing"
    ]
    your_effects = {
        "dignity": +1,
    }
    their_effects = {
        "oxygen": -1,
        "pain tolerance": -1,
    }
    flavor_text = (
        '"I fight for perfection" ~ Mike Tyson'
    )
class FlyingRoundhouse(Strike):
    your_requirements = [
        "are airborne",
        "smack a foot into them anywhere"
    ]
    your_effects = {
        "dignity": +1,
    }
    their_effects = {
        "pain tolerance": -1,
        "dignity": -1,
    }
    flavor_text = (
        '"The highest reward for a person’s toil '
        'is not what they get for it, but what they become of it." – John Ruskin'
    )
# Other
class QuickStrike(Strike):
    your_requirements = [
        "smack a hand, foot, elbow, calf or head into them anywhere"
    ]
    their_effects = {
        "senses": +1,
        "pain tolerance": -1,
    }
    flavor_text = (
        '"Take things as they are. Punch when you have to punch.\n'
        'Kick when you have to kick." ~ Bruce Lee'
    )
class KneeBomb(Strike):
    your_requirements = [
        "smack a knee into their thighs or torso"
    ]
    their_effects = {
        "pain tolerance": -1,
        "blood": -1,
    }
    flavor_text = (
        '"Do not to think of whether it ends in victory or defeat.\n'
        'Let nature take its course, and your tools\n'
        'will strike at the right moment." ~ Bruce Lee'
    )
class ElbowDagger(Strike):
    your_requirements = [
        "smack an elbow into their torso"
    ]
    your_effects = {
        "pain tolerance": -1,
    }
    their_effects = {
        "blood": -1,
        "senses": -1,
        "oxygen": -1,
    }
    flavor_text = (
        '"If God built me a ladder to heaven, I\'d climb to the top '
        'and elbow drop the world" - Mick Foley'
    )
class BashGroin(Strike):
    your_requirements = [
        "smash anything into their groin"
    ]
    your_effects = {
        "dignity": -1,
        "focus": -1,
    }
    their_effects = {
        "blood": -2,
        "pain tolerance": -2,
        "senses": -1,
        "focus": -1,
    }
    flavor_text = (
        '"My job is to hurt people."- CM Punk'
    )
class BatterKidney(Strike):
    your_requirements = [
        "smash anything into the top corner of their hip"
    ]
    your_effects = {
        "focus": -1,
    }
    their_effects = {
        "blood": -2,
        "pain tolerance": -2,
    }
    flavor_text = (
        '"He went to the hospital with bleeding kidneys.\n'
        'I went dancing with my wife." ~ George Chuvalo'
    )
class PulpBody(Strike):
    your_requirements = [
        "smash anything into their torso"
    ]
    their_effects = {
        "blood": -2,
        "pain tolerance": -1,
        "oxygen": -1,
        "stamina": +1
    }
    flavor_text = (
        '"Beat me if you can, Survive if I let you" ~ Taz'
    )
class RainBlows(Strike):
    your_requirements = [
        "smash anything into their head or torso"
    ]
    their_requirements = [
        "are sitting or prone"
    ]
    your_effects = {
        "blood": +1,
    }
    their_effects = {
        "blood": -1,
        "pain tolerance": -1,
        "senses": -2,
    }
    flavor_text = (
        '"A fighter takes a punch, and hits back with three."\n~ Roberto Duran'
    )
class HeadHarpoon(Strike):
    your_requirements = [
        "smack you head into their head",
        "are off balance or airborne"
    ]
    your_effects = {
        "blood": +1,
        "rage": +1,
        "senses": -1,
    }
    their_effects = {
        "blood": -2,
        "senses": -1,
    }
    flavor_text = (
        '"Power is not revealed by striking hard or often,\n'
        'but by striking true" ~ Balzac'
    )
class GrindingHeadbutt(Strike):
    your_requirements = [
        "sandwich their head between your head and your grasp hand"
    ]
    your_effects = {
        "stamina": +1,
        "blood": +1,
        "senses": -1,
    }
    their_effects = {
        "senses": -2,
        "pain tolerance": -1,
    }
    flavor_text = (
        '"I hear and I forget. I see and I remember. I do and I understand." '
        '~ Confucius'
    )

class Grapple(Card, ABC):
    # closer, squeezing cards
    # Want a good mix of blood/+rage (bite, scratch)
    # and oxygen/-rage (presses, squeezes)
    pass
class GougeEyes(Grapple):
    your_requirements = [
        "touch both grasp hands to their face"
    ]
    your_effects = {
        "dignity": -2,
    }
    their_effects = {
        "blood": -2,
        "senses": -2,
        "rage": +1,
    }
    flavor_text = (
        'I swear on my beautiful mother\'s eyes, if you don\'t shut up, '
        'I\'m gouging yours out." ~ Eddie Kingston'
    )
class RakeArms(Grapple):
    your_requirements = [
        "touch both grasp hands to their forearm or bicep"
    ]
    your_effects = {
        "senses": -1,
    }
    their_effects = {
        "blood": -2,
        "stamina": -1,
        "rage": +1,
    }
    flavor_text = (
        '"One could laugh at the world better if it didn\'t mix '
        'tender kindliness with its brutality." ~ D. H. Lawrence'
    )
class DesperateBite(Grapple):
    your_requirements = [
        "touch your head to them anywhere"
    ]
    your_effects = {
        "focus": -1,
        "dignity": -1,
    }
    their_effects = {
        "blood": -2,
        "pain tolerance": -1,
        "rage": +1,
    }
    flavor_text = (
        '"Your heroes are dead. I killed them."- CM Punk'
    )
class GnawFace(Grapple):
    your_requirements = [
        "touch your head to their head"
    ]
    your_effects = {
        "focus": -1,
        "senses": -1,
    }
    their_effects = {
        "blood": -1,
        "pain tolerance": -1,
        "senses": -2
    }
    flavor_text = (
        '"I Want Your Heart. I Want to Eat His Children." ~ Mike Tyson'
    )
# Chokes/presses
class NakedPress(Grapple):
    your_requirements = [
        "sandwich their neck between your forearms",
    ]
    your_effects = {
        "focus": -1,
        "dignity": +1,
    }
    their_effects = {
        "oxygen": -2,
        "senses": -1
    }
    flavor_text = (
        '"You picked a beautiful hill to die on" ~ Luke Harper'
    )
class AnacondaChoke(Grapple):
    your_requirements = [
        "are prone",
        "sandwich their neck between your forearm and chest",
    ]
    your_effects = {
        "pain tolerance": +1,
    }
    their_effects = {
        "oxygen": -2,
        "stamina": -1,
        "senses": -1
    }
    flavor_text = (
        '"You cannot blame the snake for biting you.\n'
        'You can only blame it for being a snake." ~ ᚱᛟᛒᛟᛏ'
    )
class ClockChoke(Grapple):
    your_requirements = [
        "touch a forearm to their neck",
    ]
    their_requirements = [
        "are prone"
    ]
    your_effects = {
        "focus": -1,
        "pain tolerance": +1,
    }
    their_effects = {
        "oxygen": -2,
        "rage": -2,
    }
    flavor_text = (
        '"I swear it upon Zeus: even an outstanding runner cannot be the equal'
        ' of an average wrestler." ~ Socrates'
    )
class ThumbStrangle(Grapple):
    your_requirements = [
        "touch both grasp hands to their neck",
    ]
    their_effects = {
        "oxygen": -2,
        "senses": -1,
        "dignity": +1
    }
    flavor_text = (
        '''"Send anyone you want,\n'''
        '''but don't send anyone you want back." ~ Chael Sonnen'''
    )
class TriangleSqueeze(Grapple):
    your_requirements = [
        "sandwich their torso or head between your thighs",
    ]
    your_effects = {
        "dignity": +1,
    }
    their_effects = {
        "oxygen": -2,
    }
    flavor_text = (
        '"Knowing is not enough, we must apply.\n'
        'Willing is not enough, we must do." ~ Bruce Lee'
    )
# Pain locks, other
class LegLock(Grapple):
    your_requirements = [
        "sandwich their leg or hips between your thighs",
        "touch a grasp hand to their calf or foot"
    ]
    your_effects = {
        "oxygen": +1,
        "pain tolerance": +1,
    }
    their_effects = {
        "pain tolerance": -1,
        "stamina": -1,
    }
    flavor_text = (
        '"The more you sweat in peace, the less you bleed in war." '
        '\n~ Norman Schwarzkopf'
    )
class ArmBar(Grapple):
    your_requirements = [
        "sandwich their bicep between your thighs or forearm and chest",
        "touch a grasp hand to their forearm or hand"
    ]
    your_effects = {
        "stamina": +1,
    }
    their_effects = {
        "pain tolerance": -2,
        "senses": -1,
    }
    flavor_text = (
        '"What the superior man seeks is in himself;\n'
        'what the small man seeks is in others." ~ Confucius'
    )
class WristLock(Grapple):
    your_requirements = [
        "touch a grasp hand to their hand",
        "touch a grasp hand to that forearm or bicep",
    ]
    their_requirements = [
        "are prone"
    ]
    your_effects = {
        "stamina": +1,
        "blood": +1,
    }
    their_effects = {
        "rage": +1,
        "pain tolerance": -2,
        "senses": -1,
    }
    flavor_text = (
        '"I saw his true color, and that color was yellow" ~ BJ Flores'
    )
class HangingBind(Grapple):
    your_requirements = [
        "are airborne",
        "wrap at least two limbs around them",
    ]
    their_requirements = [
        "are standing, crouching, or off balance"
    ]
    your_effects = {
        "dignity": +1,
        "stamina": +1,
    }
    their_effects = {
        "stamina": -2,
        "rage": -1,
        "oxygen": -1,
    }
    flavor_text = (
        '"To hell with circumstances; I create opportunities." ~ Bruce Lee'
    )
class SmotheringFaceGrope(Grapple):
    your_requirements = [
        "have your chest above their chest",
        "touch a grasp hand to their face"
    ]
    their_requirements = [
        "are prone or sitting"
    ]
    your_effects = {
        "rage": +1,
    }
    their_effects = {
        "stamina": -1,
        "oxygen": -1,
        "senses": -1,
    }
    flavor_text = (
        '"Next time I fight him, I will deform his face." ~ Wanderlei Silva'
    )


class PsychOut(Card, ABC):
    pass
class TapOut(PsychOut):
    your_requirements = [
        "touch a flat palm to them anywhere"
    ]
    your_effects = {
        "dignity": -1,
    }
    their_effects = {
        "rage": -1,
    }
    flavor_text = (
        '"To see a man beaten not by a better opponent\n'
        'but by himself is a tragedy." ~ Cus D\'Amato'
    )
class FauxWhiteFlag(PsychOut):
    your_requirements = [
        "lift both flat palms above your head"
    ]
    your_effects = {
        "dignity": -1,
    }
    their_effects = {
        "rage": -2,
        "dignity": +1,
    }
    flavor_text = (
        '"The psychology of brutality was worse than the beatings."\n'
        '~ John Blair'
    )
class BegAndPlead(PsychOut):
    your_requirements = [
        "are sitting or crouching",
        "touch both flat palms together"
    ]
    your_effects = {
        "dignity": -1,
        "stamina": +2,
    }
    their_effects = {
        "focus": -1,
        "rage": -1,
    }
    flavor_text = (
        '"Man, the living creature, the creating individual, '
        'is always more important than any established style or system." '
        '~ Bruce Lee'
    )
class Legerdemain(PsychOut):
    your_requirements = [
        "smack a grasp hand to them anywhere"
    ]
    your_effects = {
        "pain tolerance": +1,
    }
    their_effects = {
        "focus": -1,
        "oxygen": +1,
    }
    flavor_text = (
        '"I never wanted to be the next Bruce Lee.\n'
        'I just wanted to be the first Jackie Chan" ~ Jackie Chan'
    )
class BobAndWeave(PsychOut):
    your_requirements = [
        "standing or crouching",
        "both hands are fists",
        "have >=4 focus",
        "your torso was moved this turn",
    ]
    your_effects = {
        "senses": +1,
        "stamina": +1,
    }
    their_effects = {
        "focus": -1,
    }
    flavor_text = (
        '"Do not allow negative thoughts to enter your mind for they are '
        'the weeds that strangle confidence." ~ Bruce Lee'
    )
class SubtleTaunt(PsychOut):
    your_requirements = [
        "touch one hand to your hip",
    ]
    their_requirements = [
        "have >=4 rage",
    ]
    your_effects = {
        "senses": +1,
        "pain tolerance": +1,
        "rage": -1,
    }
    their_effects = {
        "dignity": -2,
    }
    flavor_text = (
        '"For it is easy to criticize and break down the spirit of others, '
        'but to know yourself takes a lifetime." ~ Bruce Lee'
    )
class GoadingChin(PsychOut):
    your_requirements = [
        "are not prone",
        "have both hands on-level or below their elbow",
    ]
    their_requirements = [
        "have >=5 rage",
    ]
    your_effects = {
        "stamina": +1,
    }
    their_effects = {
        "rage": -3,
    }
    flavor_text = (
        '''"You're just an average bloke,\nI'm a fucking samurai." '''
        '~ Luke Rockhold'
    )
class HurlObsecenites(PsychOut):
    your_requirements = [
        "have >=4 oxygen"
    ]
    their_requirements = [
        "have <=4 dignity"
    ]
    your_effects = {
        "rage": +1,
        "focus": +1,
    }
    their_effects = {
        "focus": -1,
    }
    flavor_text = (
        '"If you don\'t want to slip up tomorrow,\nspeak the truth today." '
        '~ Bruce Lee'
    )
class OpenlyJeer(PsychOut):
    your_requirements = [
        "have >=4 rage and >=4 blood",
    ]
    their_requirements = [
        "have >=4 rage"
    ]
    your_effects = {
        "senses": +1,
        "oxygen": +1,
        "pain tolerance": +1,
    }
    their_effects = {
        "focus": -1,
    }
    flavor_text = (
        '''"If you even dream of beating me\n'''
        '''you'd better wake up and apologize." ~ Muhammad Ali'''
    )
class SternWord(PsychOut):
    your_requirements = [
        "touch a grasp hand to their arm",
        "have >=4 dignity"
    ]
    your_effects = {
        "focus": +1
    }
    their_effects = {
        "dignity": -2,
    }
    flavor_text = (
        '"If a man has enough power, he can speak softly\n'
        'and everyone will listen" ~ Jake Roberts'
    )
class SnideSnort(PsychOut):
    your_requirements = [
        "have >=4 rage"
    ]
    your_effects = {
        "blood": +1,
        "oxygen": -1,
    }
    their_effects = {
        "dignity": -1,
    }
    flavor_text = (
        '"A quick temper will make a fool of you soon enough."\n~ Bruce Lee'
    )
class CrushPedistal(PsychOut):
    your_requirements = [
        "touch one foot to their chest",
        "your hips are over their torso",
    ]
    their_requirements = [
        "prone or sitting"
    ]
    your_effects = {
        "dignity": +1,
        "blood": +1,
    }
    their_effects = {
        "oxygen": -2,
    }
    flavor_text = (
        '''"If we fight for money, I'll stop hitting you when you ask me to.\n'''
        '''If we fight for honor, I'll stop when I feel like it." '''
        '~ Rickson Gracie'
    )
class FistfulOfHair(PsychOut):
    your_requirements = [
        "touch a grasp hand to their head",
    ]
    their_requirements = [
        "are crouching, sitting or prone "
    ]
    your_effects = {
        "rage": +1,
        "focus": +1,
    }
    their_effects = {
        "oxygen": +1,
        "senses": -1,
    }
    flavor_text = (
        '"Do you think I’m just going to sit there\n'
        'and let you kill me?" ~ Daniel Cormier'
    )
class FeedOff(PsychOut):
    your_effects = {
        "rage": +1,
        "blood": +1,
    }
    their_effects = {
        "rage": +1,
        "blood": +1,
    }
    flavor_text = (
        '"I speak the language of violence,\n'
        'but I\'m also pretty good with words." ~ Jon Moxley'
    )

class Pose(Card, ABC):
    # take a stance to help yourself
    pass
class LowSprawl(Pose):
    your_requirements = [
        "are prone",
        "fully extend two or more limbs",
    ]
    your_effects = {
        "focus": +1,
        "oxygen": +1,
    }
    flavor_text = (
        '"The hero and the coward both feel the same thing.\n'
        '''The hero uses his fear, while the coward runs. It's the same thing, '''
        '''but it's what you do with it." ~ Cus D'Amato'''
    )
class Zenkutsu(Pose):
    your_requirements = [
        "are crouching, with feet spaced >= a limb-length apart",
        "have both hands between your waist-height and chest-height",
    ]
    your_effects = {
        "focus": -1,
        "senses": +1,
    }
    their_effects = {
        "dignity": -1,
    }
    flavor_text = (
        '"Truth has no path. Truth is living and, therefore, changing."\n'
        '~ Bruce Lee'
    )
class Mabu(Pose):
    your_requirements = [
        "are crouching, with feet parallel",
        "have both hands at or below your waist",
    ]
    your_effects = {
        "senses": +1,
        "rage": -1,
    }
    their_effects = {
        "dignity": -1,
    }
    flavor_text = (
        '"A wise man can learn more from a foolish question\n'
        'than a fool can learn from a wise answer." ~ Bruce Lee'
    )
class GulpAir(Pose):
    your_requirements = [
        "are standing or crouching",
        "touch a hand to your knees",
    ]
    your_effects = {
        "focus": +1,
        "oxygen": +2,
        "senses": -1,
    }
    flavor_text = (
        '''"Once that bell rings you're on your own.\n'''
        '''It's just you and the other guy." ~ Joe Louis'''
    )
class RawHowl(Pose):
    your_effects = {
        "stamina": +2,
        "oxygen": -1,
        "senses": -1,
    }
    flavor_text = (
        '''"I'm going to beat you into a living death!" ~ Ken Shamrock'''
    )
class GutteralSob(Pose):
    your_requirements = [
        "are crouching, sitting, prone, or off balance",
        "have >=3 oxygen",
    ]
    your_effects = {
        "blood": +1,
        "pain tolerance": +1,
    }
    flavor_text = (
        '''"It's only pain. It will not hurt you." ~ Bas Rutten'''
    )
class SlowBreathing(Pose):
    your_requirements = [
        "are standing or crouching",
        "touch one hand to your chest",
        "have >=4 oxygen",
    ]
    your_effects = {
        "focus": +1,
        "stamina": +2,
        "blood": +1,
    }
    flavor_text = (
        '"Life itself is your teacher,\n'
        'and you are in a state of constant learning." ~ Bruce Lee'
    )
class LionsBreath(Pose):
    @classmethod
    def human_name(cls):
        return "Lion's Breath"

    your_requirements = [
        "have >=5 oxygen",
    ]
    your_effects = {
        "rage": +1,
        "blood": +1,
    }
    flavor_text = (
        '"Using no way as a way,\nhaving no limitation as limitation." '
        '~ Bruce Lee'
    )
class CrossGaurd(Pose):
    your_requirements = [
        "place both forearms between your chest and theirs",
    ]
    your_effects = {
        "oxygen": +1,
        "dignity": +1,
        "rage": -1,
    }
    flavor_text = (
        '"To know oneself is to study oneself '
        'in action with another person." ~ Bruce Lee'
    )
    flavor_text = (
        '"Ideas are the great warriors of the world, '
        'and a war that has no idea behind it, is simply a brutality." ~ James A. Garfield'
    )
class Vasoconstrict(Pose):
    your_requirements = [
        "are prone",
        "at least one limb fully extended"
    ]
    your_effects = {
        "blood": +2,
        "rage": -1,
        "focus": +1
    }
    flavor_text = (
        '"There are no limits. There are plateaus, but you must not stay there, '
        'you must go beyond them. If it kills you, it kills you."\n~ Bruce Lee'
    )
class FetalCurl(Pose):
    your_requirements = [
        "are prone",
        "at least two feet or hands touching torso or head"
    ]
    your_effects = {
        "blood": +1,
        "stamina": +1,
        "focus": +1,
    }
    flavor_text = (
        '"Everybody got a plan\n'
        '\'til they get punched in the face." - Mike Tyson'
    )
class StayDown(Pose):
    your_requirements = [
        "are prone",
        "have <=3 blood or <=3 pain tolerance"
    ]
    your_effects = {
        "stamina": +1,
        "focus": +1,
        "blood": +1,
        "pain tolerance": +1,
    }
    flavor_text = (
        '"When he knocked me down\nI could have stayed there for three weeks." '
        '~ James J Braddock'
    )
class CoverUp(Pose):
    your_requirements = [
        "touch both fists and forearms to your head"
    ]
    your_effects = {
        "rage": -1,
        "focus": +1,
        "pain tolerance": +1,
    }
    flavor_text = (
        '"A black belt only covers 2 inches of your ass,\n'
        'the rest is up to you."~ Royce Gracie'
    )
class StayGrounded(Pose):
    your_requirements = [
        "are standing or crouching",
        "have <=4 rage",
        "have >=3 focus",
    ]
    your_effects = {
        "pain tolerance": +1,
        "dignity": +1,
        "focus": +2
    }
    flavor_text = (
        '"Life is really simple,\nbut we insist on making it complicated." '
        '~ Confucius'
    )
class BodyScan(Pose):
    your_requirements = [
        "have >=5 focus",
        "you and them are not touching",
    ]
    your_effects = {
        "senses": +2,
        "dignity": +1,
    }
    flavor_text = (
        '"The successful warrior is the average man,\n'
        'with laser-like focus." ~ Bruce Lee'
    )
class ShareAir(Pose):
    your_requirements = [
        "have <=4 rage and >=3 dignity",
        "your torso is <= a forearm-length from theirs",
    ]
    your_effects = {
        "focus": +1,
        "stamina": +1,
        "senses": +1,
    }
    their_effects = {
        "oxygen": +1,
    }
    flavor_text = (
        '"By nature, humans are nearly alike;\nby practice, '
        'they get to be wide apart." ~ Confucius'
    )

class Control(Card, ABC):
    # grab them to move them
    pass
class SqueezeWrist(Control):
    your_requirements = [
        "touch a grasp hand to their hand or forearm"
    ]
    your_effects = {
        "focus": -1,
        "stamina": -1,
    }
    extra_effects = "You can move that limb any way you like"
    flavor_text = (
        '"The best fighter is someone who never has to fight '
        'because they control the situation." - Bruce Lee'
    )
class SlapAway(Control):
    your_requirements = [
        "smack a flat palm into their forearm"
    ]
    your_effects = {
        "focus": -1,
    }
    extra_effects = "You can move that limb any way you like"
    flavor_text = (
        '"It\'s not the daily increase but daily decrease.\n'
        'Hack away at the unessential." ~ Bruce Lee'
    )
class SweepLeg(Control):
    your_requirements = [
        "smash a foot into their calf"
    ]
    your_effects = {
        "stamina": -1,
    }
    their_effects = {
        "pain tolerance": -1,
    }
    extra_effects = "You can move that limb any way you like"
    flavor_text = (
        '"If you screw things up in tennis, it\'s 15-love.\n'
        'If you screw up in boxing, it\'s your ass." ~ Randall "Tex" Cobb'
    )
class DoorKick(Control):
    your_requirements = [
        "smash a foot into their hip"
    ]
    your_effects = {
        "stamina": -1,
    }
    their_effects = {
        "blood": -1
    }
    extra_effects = (
        "You can move their hips a limb-length away.\n"
        "Any part on the ground tries to stay in place."
    )
    flavor_text = (
        '"I made a lot of mistakes out of the ring,\n'
        'but I never made any in it." ~ Jack Johnson'
    )
class ChokeSlam(Control):
    your_requirements = [
        "are standing",
        "touch a grasp hand to their neck",
        "have >=4 stamina"
    ]
    their_effects = {
        "oxygen": -1,
        "senses": -1,
    }
    extra_effects = (
        "Move them and yourself to a prone position.\n"
        "Any part on the ground tries to stay in place."
    )
    flavor_text = (
        '"No one makes it out of this sport\n'
        'without taking an ass whoopin." ~ Nick Diaz'
    )
class LeapingTackle(Control):
    your_requirements = [
        "are crouching and have >=4 stamina",
        "have both grasp hands infront of your chest",
    ]
    your_effects = {
        "oxygen": -1,
    }
    their_effects = {
        "rage": -1,
        "senses": -1,
    }
    extra_effects = (
        "Move them and yourself to a prone position.\n"
        "Any parts on the ground try to stay in place."
    )
    flavor_text = (
        '"You better give your soul to the lord,\n'
        'cause your ass belongs to me." - Undertaker'
    )
class ShoulderSlam(Control):
    your_requirements = [
        "smack your torso or bicep into their torso",
    ]
    your_effects = {
        "oxygen": -1,
    }
    their_effects = {
    }
    extra_effects = (
        "You can move their hips a forearm-length away.\n"
        "Any part on the ground tries to stay in place."
    )
    flavor_text = (
        '"Act like a man of thought – Think like a man of action."\n'
        '~ Thomas Mann'
    )
class Powerslam(Control):
    your_requirements = [
        "touch them anywhere with a grasp hand",
    ]
    their_requirements = [
        "are airborne"
    ]
    their_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Rotate and lower them to a prone position.\n"
    )
    flavor_text = (
        '"In the midst of chaos, there is also opportunity." ~ Sun Tzu'
    )
class CannonBall(Control):
    your_requirements = [
        "are airborne",
        "smack your torso into them anywhere",
    ]
    their_effects = {
        "focus": -1,
    }
    extra_effects = (
        "Rotate and lower them to a prone position.\n"
    )
    flavor_text = (
        '''"I'm not God, but I am something similar."\n~ Roberto Duran'''
    )
class LightShove(Control):
    your_requirements = [
        "touch a flat palm to their torso"
    ]
    their_requirements = [
        "are standing, crouching, or off balance"
    ]
    your_effects = {
        "senses": +1,
        "oxygen": +1,
    }
    their_effects = {
        "blood": +1,
    }
    extra_effects = (
        "If they are off balance,\nmove them to a prone position."
    )
    flavor_text = (
        '"Obstacles cannot crush me;\n'
        'every obstacle yields to stern resolve"\n'
        '~ Leonardo Da Vinci'
    )

class Movement(Card, ABC):
    # TODO better name?
    pass
class TuckJump(Movement):
    your_requirements = [
        "lift both feet above knee-level"
    ]
    your_effects = {
        "oxygen": -1,
        "stamina": +1,
        "senses": +1,
    }
    flavor_text = (
        '"Take no thought of who is right or wrong or who is better than. '
        'Be not for or against." ~ Bruce Lee'
    )
class HighJump(Movement):
    your_requirements = [
        "are crouching"
    ]
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Move your hips a limb-length in any direction"
    )
    flavor_text = (
        '"What we do in life echoes in eternity." ~ Maximus'
    )
class Spin(Movement):
    your_requirements = [
        "are standing, crouching, or sitting"
    ]
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Rotate your character 180 around the hips"
    )
    flavor_text = (
        '''"There's 3 things in life that excite me. A woman, of course.\n'''
        '''Dinosaurs, and the violence of the Octagon" - Georges St-Pierre'''
    )
class KickBack(Movement):
    your_requirements = [
        "are crouching, sitting, or prone",
        "touch a foot to their torso",
    ]
    your_effects = {
        "senses": +1,
        "stamina": +1,
    }
    their_effects = {
        "senses": +1,
        "focus": +1,
    }
    extra_effects = (
        "Move your hips a limb-length away"
    )
    flavor_text = (
        '"A warrior never worries about his fear." ~ Carlos Castaneda'
    )
class KipUp(Movement):
    your_requirements = [
        "are prone",
        "touch both hands to the ground",
        "you and them are not touching"
    ]
    your_effects = {
        "stamina": -1,
        "dignity": +2,
        "oxygen": +1,
    }
    extra_effects = (
        "Move your hips a limb-length up, keeping your feet on the ground"
    )
    flavor_text = (
        '"The spirit of a warrior never breaks, it only bends."'
        '\n~ Sable Nightshade*'
    )

class Reaction(Card, ABC):
    # Card played on their turn
    # TODO is this a good idea?
    pass
# Responses to strikes
class CatchPunch(Reaction):
    your_requirements = [
        "can have a grasp hand to touch their fist"
    ]
    their_requirements = [
        "are smacking/smashing with a fist"
    ]
    your_effects = {
        "focus": -1,
        "stamina": -1,
    }
    extra_effects = (
        "Negate their card's effects on you"
    )
    flavor_text = (
        '"Conceive. Believe. Achieve. Shut the fuck up!"\n~ Buddeh Bisping'
    )
class UkeBlock(Reaction):
    your_requirements = [
        "can have your forearm touch their hand"
    ]
    their_requirements = [
        "are smacking/smashing with a hand"
    ]
    your_effects = {
        "senses": -1,
        "pain tolerance": -1,
    }
    extra_effects = (
        "Negate their card's effects on you"
    )
    flavor_text = (
        '''"Its tough to get up and fight\n'''
        '''if you've been sleeping in silk pajamas." ~ Marvin Hagler'''
    )
class FirmRepost(Reaction):
    your_requirements = [
        "can smash your fist into their torso",
    ]
    their_requirements = [
        "are smacking/smashing you"
    ]
    your_effects = {
        "senses": -1,
    }
    their_effects = {
        "oxygen": -2,
        "focus": -1,
        "stamina": -2,
    }
    flavor_text = (
        '"Every battle scars, but also shapes." ~ Nero Voss*'
    )
class GetThereFirst(Reaction):
    your_requirements = [
        "can smack your fist into their head",
    ]
    their_requirements = [
        "are smacking/smashing you"
    ]
    extra_effects = (
        "Negate their card's effects on you"
    )
    your_effects = {
        "focus": -1,
    }
    their_effects = {
        "senses": -1,
    }
    flavor_text = (
        '"Cry in the dojo, laugh on the battlefield." ~ uri Pazarán'
    )
class RetreatingShrimp(Reaction):
    your_requirements = [
        "are prone"
    ]
    their_requirements = [
        "are grappling you"
    ]
    their_effects = {
        "stamina": +1,
    }
    extra_effects = (
        "Move your hips a limb-length away"
    )
    flavor_text = (
        '"Notice that the stiffest tree is most easily cracked,\n'
        'while the bamboo or willow survives by bending with the wind."\n'
        '~ Bruce Lee'
    )
class ChinUp(Reaction):
    their_requirements = [
        "are touch/smack/smashing you"
    ]
    your_effects = {
        "blood": -1,
        "dignity": +1,
        "pain tolerance": +1,
    }
    their_effects = {
        "rage": +1
    }
    flavor_text = (
        '"Do not pray for an easy life,\n'
        'pray for the strength to endure a difficult one." ~ Bruce Lee'
    )
class SharpInhale(Reaction):
    their_requirements = [
        "are touch/smack/smashing you"
    ]
    your_effects = {
        "oxygen": +2,
    }
    their_effects = {
        "rage": +1
    }
    flavor_text = (
        '"Life is a fight from the minute you take your first breath\n'
        'to the moment you exhale your last." ~ Ronda Rousey'
    )
class ClenchTeeth(Reaction):
    their_requirements = [
        "are touch/smack/smashing you"
    ]
    your_effects = {
        "stamina": +2,
        "pain tolerance": -1,
        "blood": -1,
    }
    flavor_text = (
        '"In the middle of difficulty lies opportunity." ~ Bruce Lee'
    )
class GirdLoins(Reaction):
    their_requirements = [
        "are touch/smack/smashing your torso"
    ]
    your_effects = {
        "stamina": +1,
        "oxygen": +1,
        "blood": +1,
    }
    their_effects = {
        "focus": +1,
        "stamina": +1,
    }
    flavor_text = (
        '"Not. Good." ~ FarFar Karlsson'
    )
class FlowLikeWater(Reaction):
    their_requirements = [
        "are smack/smashing you"
    ]
    your_effects = {
        "blood": -2,
    }
    their_effects = {
        "stamina": -2,
        "pain tolerance": +1,
    }
    extra_effects = "Move the limb that was struck any way you like"
    flavor_text = (
        '"Empty your mind, be formless, shapeless." ~ Bruce Lee'
    )
class AnalyticReappraisal(Reaction):
    your_requirements = [
        "have <=3 pain tolerance"
    ]
    their_requirements = [
        "are smack/smashing you"
    ]
    your_effects = {
        "pain tolerance": +2,
        "senses": +2,
        "focus": -1,
    }
    their_effects = {
        "rage": -1,
    }
    flavor_text = (
        '"Pain is only a sensation." ~ FarFar Karlsson'
    )
class DragNails(Reaction):
    your_requirements = [
        "can touch a grasp hand to them anywhere",
    ]
    their_requirements = [
        "are touch/smack/smashing you"
    ]
    your_effects = {
        "stamina": -1,
        "dignity": -1,
    }
    their_effects = {
        "pain tolerance": +1,
        "blood": -2,
        "stamina": -1,
    }
    flavor_text = (
        '"Victory is reserved for those who are willing to pay its price."\n'
        '~ Sun Tzu'
    )
# Responses to poses/psych outs
class KnowingSmirk(Reaction):
    their_requirements = [
        "are posing or psyching you out"
    ]
    your_effects = {
        "dignity": +1,
        "senses": +1,
        "focus": -2,
    }
    flavor_text = (
        '"All types of knowledge, ultimately mean self-knowledge."'
        '\n~ Bruce Lee'
    )
class CatchBreath(Reaction):
    their_requirements = [
        "are posing or psyching you out"
    ]
    your_effects = {
        "oxygen": +2
    }
    their_effects = {
        "focus": +1
    }
    flavor_text = (
        '"Absorb what is useful, discard what is not,\n'
        'add what is uniquely your own." ~ Bruce Lee'
    )
class DeflatingGlare(Reaction):
    their_requirements = [
        "are posing or psyching you out",
        "they will have >=4 stamina"
    ]
    their_effects = {
        "stamina": -2
    }
    flavor_text = (
        '"Why would I hold him down\nwhen I can just stare him down?" ~ Hendo'
    )

class Rule(Card, ABC):
    flavor_text = ""
class MoveLimb(Rule):
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Move one of your limbs any way you like\n"
        "<i class='reminder'>A limb includes all joints up to the hips, e.g:"
        "hand+forearm+bicep+torso+hips or foot+calf+thigh+hips.</i>"
        "<hr>"
        "Keep this card in on the table always\n"
        "You can play it multiple times a turn"
    )
class ContactRules(Rule):
    extra_effects = (
        "Most cards require some kind of contact. smack/smash require that "
        "the limb has moved during this turn to get to it's destination:"
        "<hr>"
        "smack - moved at least a forearm-length\n"
        "smash - moved at least a limb-length \n"
        "<i class='reminder'>a smack/smash can only be 'claimed' on one card,\n"
        "i.e, you can't simultaneously Knuckle Strike and Bloody Nose.</i>"
    )
class SwitchGrip(Rule):
    your_effects = {
        "focus": -1,
    }
    extra_effects = (
        "Change out one or both hands<hr>"
        "Keep this card in on the table always\n"
        "You can play it multiple times a turn"
    )
class KeepBreathing(Rule):
    extra_effects = (
        "At the start of your turn,\n"
        "gain focus and stamina from your stance:<hr>"
        f"{'<hr>'.join(s.get_description() for s in Card.stances.values())}"
        "<hr><i class='reminder'> Whenever a pose is could be multiple,\n"
        "the card-player can choose which.</i>"
    )
class FightIgnition(Rule):
    from src.anubis import Anubis
    extra_effects = f"""
        <b> To start playing: </b>
        * Each player draws <b>{Anubis.draw_size}</b> Action Cards
        * Each player lays, face down, one of each Loss Card (8 total)
        * Place a d6 on each Loss Card, each starting at <b>6</b>
        * Lay out these <b>Rule</b> reminder cards on the table
        * Place the figures in their stand, upright,
        with hands/arms however you like.
        <i class='reminder'> Whichever player has the biggest bruise goes first.
        If neither is bruised, whomever bled last. </i>
        """
class YourTurn(Rule):
    from src.anubis import Anubis
    extra_effects = f"""
        <b> Start your turn: </b>
        * Draw until you have <b>{Anubis.draw_size}</b> cards
        * Check <b>Keep Breathing</b> to see how much stamina/focus you recover
        * If you are airborne, move downwards until some part of you touches the ground
        <i class='reminder'>You can, however, be airborne during and after your turn
        (and thus during your opponent's)</i>
        <hr><b> During your turn: </b>
        * Use stamina/focus to <b>Move Limb</b>s/<b>Switch Grip</b>
        * Play as many cards as you like
        * Discard any you don't want
        <hr><b> During theirs: </b>
        * <b>Reaction</b> cards are played in response to an opponent's card
        <i class='reminder'> Some may require you to <b>Move Limb</b>s/<b>Switch Grip</b>
        - which still costs stamina/focus. </i>
        <hr> Stats cannot be raised above <b>6</b>
        Fight ends when any status is reduced to <b class='minus'>0</b>:
        Flip over that Loss Card, and read out your defeat.
    """
# class YourHealth(Rule):
#     extra_effects = (
#         "Place a d6 to keep track of each of your statuses.\n"
#         "They cannot go above 6.\n"
#         "If they ever go below 1, draw the loss card to see how the fight ends"
#     )
# class ZZTest(Rule):
#     your_requirements = [
#         "smash a foot into their neck",
#         ">=2 oxygen",
#         ">=3 oxygen",
#         ">=4 oxygen",
#         ">=5 oxygen",
#         ">=6 oxygen",

#         "<=2 focus",
#         "<=3 focus",
#         "<=4 focus",
#         "<=5 focus",
#         "<=6 focus",
#     ]

# Card ideas:
"""
Feint
Taunt - raise their rage. If high enough, they 'red out' and...
focus drops to 2?
'float' - move out of the way when they smack/smash, negate
drunken master - bonus for being off balance
crush windpipe - mix of throat punch and thumb strangle, like clinch punch
judo flip - control reaction
Sticky Hands - reaction to get oxy/pain, at the cost of focus. Like legerdemain?

Would introduce 'card meta stuff' - but I have some interest in
'reveal X cards to player' as a way of 'being predictable',
but also players could use to trick/feint.
...

Revisit stats:
headbutts can take up some of the -senses to player
maybe control cards give +oxy to enemy, because it takes a second to judo flip?
Maybe basic attacks can give +1 focus
How we doing on categories
...

TODO could have a card that is like
'What happens when you go over 6', and for each it is like:

Overfull Lungs: -1 pain tolerance
Overstimulated Blood: nothing
Numb to Pain: focus +1
Hyper-aware: focus -1
Maddening Rage: focus -1
Haughty Dignity: blood -1
Hyper-focused: rage -1, dignity +1
Exhilarating Stamina: nothing

Could rename 'vasoconstrict' something more lkke
'draw blood to core' -but vaso sounds coool

Could add a thing to reaction cards that require movement that is like:
'You may play <b>Move Limb</b>/<b>Switch Grip</b>',
then have the requirements more 'normally'
"""
