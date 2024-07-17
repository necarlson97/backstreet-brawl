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
class CheekSlap(Strike):
    your_requirements = [
        "smack a flat palm into their face"
    ]
    their_effects = {
        "senses": +1,
        "rage": -2,
        "pain tolerance": -1,
    }
class FrontJab(Strike):
    your_requirements = [
        "smack a fist into them anywhere"
    ]
    your_effects = {
        "focus": -1,
    }
    their_effects = {
        "stamina": -2,
        "senses": +1,
        "pain tolerance": -1,
    }
class Knifehand(Strike):
    your_requirements = [
        "smash a flat palm into their neck"
    ]
    your_effects = {
        "stamina": -1,
        "focus": +1,
    }
    their_effects = {
        "oxygen": -2,
        "focus": -1,
        "senses": -1,
    }
class Hammerfist(Strike):
    your_requirements = [
        "smack a fist into their head"
    ]
    their_requirements = [
        "are sitting or prone"
    ]
    your_effects = {
        "stamina": -1,
        "rage": +1,
    }
    their_effects = {
        "blood": -2,
        "senses": -2,
    }
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
class SolidHook(Strike):
    your_requirements = [
        "smack a fist into them anywhere",
        "have your elbow on-level with that fist"
    ]
    your_effects = {
        "stamina": -1,
    }
    their_effects = {
        "pain tolerance": -1,
        "blood": -1,
    }
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
# Kicks
class Curbstomp(Strike):
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
# Other
class KneeBomb(Strike):
    your_requirements = [
        "smack a knee into their thighs or torso",
        "have the other leg extended behind you"
    ]
    your_effects = {
    }
    their_effects = {
        "pain tolerance": -1,
        "blood": -1,
    }
class ElbowDagger(Strike):
    your_requirements = [
        "smack an elbow into their torso"
    ]
    your_effects = {
        "pain tolerance": -1,
    }
    their_effects = {
        "blood": -1,
        "senses": -2,
    }
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
class LightShove(Strike):
    your_requirements = [
        "touch a flat palm to their torso"
    ]
    their_requirements = [
        "are standing or crouching"
    ]
    your_effects = {
        "senses": +2,
        "oxygen": +1,
    }
    their_effects = {
        "blood": +1,
    }

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
class RakeArms(Grapple):
    your_requirements = [
        "touch both grasp hands to their forearm or bicep"
    ]
    your_effects = {
        "stamina": -1,
    }
    their_effects = {
        "blood": -2,
        "stamina": -1,
        "rage": +1,
    }
class DesperateBite(Grapple):
    your_requirements = [
        "touch your head to them anywhere"
    ]
    your_effects = {
        "focus": -2,
    }
    their_effects = {
        "blood": -2,
        "pain tolerance": -1,
        "rage": +1,
    }
class GnawFace(Grapple):
    your_requirements = [
        "touch your head to their head"
    ]
    your_effects = {
        "focus": -1,
        "dignity": -1,
    }
    their_effects = {
        "blood": -1,
        "pain tolerance": -1,
        "senses": -2
    }
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
class ThumbStrangle(Grapple):
    your_requirements = [
        "touch both grasp hands to their neck",
    ]
    their_effects = {
        "oxygen": -2,
        "senses": -1,
        "dignity": +1
    }
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
# Pain locks, other
class LegLock(Grapple):
    your_requirements = [
        "sandwich their leg or hips between your thighs",
        "touch a grasp hand to their calf or foot"
    ]
    your_effects = {
        "focus": +1,
        "pain tolerance": +1,
    }
    their_effects = {
        "pain tolerance": -1,
        "senses": -1,
    }
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
class Legerdemain(PsychOut):
    your_requirements = [
        "smack a grasp hand to them anywhere"
    ]
    your_effects = {
    }
    their_effects = {
        "focus": -1,
    }
class BobAndWeave(PsychOut):
    your_requirements = [
        "standing or crouching",
        "both hands are fists",
        "have focus >3",
    ]
    your_effects = {
        "senses": +1
    }
    their_effects = {
        "focus": -1,
    }
class SubtleTaunt(PsychOut):
    your_requirements = [
        "touch one hand to your hip",
    ]
    their_requirements = [
        "have >3 anger",
    ]
    your_effects = {
        "senses": +1,
        "dignity": +1,
        "anger": -1,
    }
    their_effects = {
        "dignity": -1,
    }
class HurlObsecenites(PsychOut):
    your_requirements = [
        "have >3 oxygen"
    ]
    their_requirements = [
        "have <5 dignity"
    ]
    your_effects = {
        "rage": +1,
        "focus": +1,
    }
    their_effects = {
        "focus": -1,
    }
class OpenlyJeer(PsychOut):
    your_requirements = [
        "have >3 rage",
        "have >3 blood",
    ]
    their_requirements = [
        "have >3 rage"
    ]
    your_effects = {
        "senses": +1,
        "oxygen": +1,
        "pain tolerance": +1,
    }
    their_effects = {
        "focus": -1,
    }
class SternWord(PsychOut):
    your_requirements = [
        "touch a grasp hand to their arm",
        "have >3 dignity"
    ]
    your_effects = {
        "focus": +1
    }
    their_effects = {
        "dignity": -2,
    }
class SharpSnort(PsychOut):
    your_requirements = [
        "have >3 rage"
    ]
    your_effects = {
        "blood": +1,
        "oxygen": -1,
    }
    their_effects = {
        "senses": -1,
    }

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
class Zenkutsu(Pose):
    your_requirements = [
        "are crouching, with one foot far forward and one far back",
        "have both hands between your waist-height and chest-height",
    ]
    your_effects = {
        "focus": -1,
        "senses": +1,
    }
    their_effects = {
        "dignity": -1,
    }
class Mabu(Pose):
    your_requirements = [
        "are crouching, with feet parallel",
        "have both hands below waist-height",
    ]
    your_effects = {
        "senses": +1,
        "rage": -1,
    }
    their_effects = {
        "dignity": -1,
    }
class GulpAir(Pose):
    your_requirements = [
        "are standing or crouching",
        "touch both hands to your knees",
    ]
    your_effects = {
        "focus": +1,
        "oxygen": +2,
        "senses": -1,
    }
class SlowBreathing(Pose):
    your_requirements = [
        "are standing or crouching",
        "touch one hand to your chest",
        "have >3 oxygen",
    ]
    your_effects = {
        "focus": +1,
        "stamina": +1,
        "blood": +2,
    }
class LionsBreath(Pose):
    @classmethod
    def human_name(cls):
        return "Lion's Breath"

    your_requirements = [
        "have >4 oxygen",
    ]
    your_effects = {
        "rage": +1,
        "blood": +1,
    }
class CrossGaurd(Pose):
    your_requirements = [
        "place both forearms between your chest and theirs",
    ]
    your_effects = {
        "oxygen": +1,
        "dignity": +1,
        "rage": -1,
    }
class Vasoconstrict(Pose):
    your_requirements = [
        "prone",
        "at least one limb fully extended"
    ]
    your_effects = {
        "blood": +2,
        "rage": -1,
        "focus": +1
    }
class FetalCurl(Pose):
    your_requirements = [
        "prone",
        "at least two feet or hands touching torso or head"
    ]
    your_effects = {
        "blood": +1,
        "stamina": +1,
        "focus": +1,
    }
class CoverUp(Pose):
    your_requirements = [
        "touch both fists and forearms to your head"
    ]
    your_effects = {
        "rage": -1,
        "focus": +1,
        "pain tolerance": +1,
    }
class StayGrounded(Pose):
    your_requirements = [
        "are standing or crouching",
        "have <5 rage",
        "have >2 focus",
    ]
    your_effects = {
        "pain tolerance": +1,
        "dignity": +1,
        "focus": +2
    }
class BodyScan(Pose):
    your_requirements = [
        "are not touching them",
        "have >4 focus",
    ]
    your_effects = {
        "senses": +2,
        "dignity": +1,
    }

# Other
class CrushPedistal(Pose):
    your_requirements = [
        "touch one foot to their chest",
        "your hips are over their torso",
    ]
    your_effects = {
        "dignity": +1,
    }
    their_effects = {
        "oxygen": -1,
    }

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
class SlapAway(Control):
    your_requirements = [
        "smack a flat palm into their forearm"
    ]
    your_effects = {
        "focus": -1,
    }
    extra_effects = "You can move that limb any way you like"
class SweepLeg(Control):
    your_requirements = [
        "smash a foot into their calf"
    ]
    your_effects = {
        "stamina": -1,
    }
    their_effects = {
        "pain tolerance": -1
    }
    extra_effects = "You can move that limb any way you like"
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
        "Any part touching the ground tries to stay in place."
    )
class ChokeSlam(Control):
    your_requirements = [
        "are standing",
        "touch a grasp hand to their neck",
        "have >4 stamina"
    ]
    their_effects = {
        "oxygen": -1,
        "senses": -1,
    }
    extra_effects = (
        "Move them and yourself to a prone position.\n"
        "Any part touching the ground tries to stay in place."
    )
class Tackle(Control):
    your_requirements = [
        "are crouching and have >4 stamina",
        "have both grasp hands infront of your chest",
    ]
    your_effects = {
        "oxygen": -2,
    }
    their_effects = {
        "rage": -1,
        "senses": -1,
    }
    extra_effects = (
        "Move them and yourself to a prone position.\n"
        "Any of their parts touching the ground try to stay in place."
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
        "stamina": +1
    }
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
class KickAwway(Movement):
    your_requirements = [
        "are crouching, sitting, or prone",
        "touch a foot to their torso",
    ]
    your_effects = {
        "senses": -1,
        "stamina": +1,
    }
    extra_effects = (
        "Move your hips a limb-length away"
    )

class Reaction(Card, ABC):
    # Card played on their turn
    # TODO is this a good idea?
    pass
# Responses to strikes
class CatchPunch(Reaction):
    your_requirements = [
        "can have a grasp hand to touch their fist in one motion"
    ]
    their_requirements = [
        "are smacking/smashing you with a fist"
    ]
    your_effects = {
        "focus": -1,
        "stamina": -1,
    }
    extra_effects = (
        "Negate their card's effects on you"
    )
class UkeBlock(Reaction):
    your_requirements = [
        "can have your forearm touch their hand in one motion"
    ]
    their_requirements = [
        "are smacking/smashing you with a hand"
    ]
    your_effects = {
        "senses": -1,
        "pain tolerance": -1,
    }
    extra_effects = (
        "Negate their card's effects on you"
    )
class FirmRepost(Reaction):
    your_requirements = [
        "can smash your fist into their torso in one motion",
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
class RetreatingShrimp(Reaction):
    your_requirements = [
        "prone"
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
class ClenchTeeth(Reaction):
    their_requirements = [
        "are touch/smack/smashing you"
    ]
    # TODO
    your_effects = {
        "stamina": +2,
        "pain tolerance": -1,
        "blood": -1,
    }
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
# Responses to poses/psych outs
class KnowingSmirk(Reaction):
    their_requirements = [
        "are posing or psyching you out"
    ]
    # TODO
    your_effects = {
    }
    their_effects = {
        "dignity": +1
    }
class CatchBreath(Reaction):
    their_requirements = [
        "are posing or psyching you out"
    ]
    # TODO
    your_effects = {
        "oxygen": +2
    }
    their_effects = {
        "focus": +1
    }
class DeflatingGlare(Reaction):
    their_requirements = [
        "are posing or psyching you out",
        "they will have >3 stamina"
    ]
    their_effects = {
        "stamina": -2
    }

class Rule(Card, ABC):
    pass
class MoveLimb(Rule):
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Move one of your limbs any way you like\n"
        "<i class='reminder'>A limb includes many joints, e.g.: "
        "wrist+elbow+shoulder. The head+torso+hips is also a limb.</i>"
        "<hr>"
        "Keep this card in your hand always\n"
        "You can play it multiple times a turn"
    )
class SwitchGrip(Rule):
    your_effects = {
        "stamina": -1,
    }
    extra_effects = (
        "Change out one or both hands<hr>"
        "Keep this card in your hand always\n"
        "You can play it multiple times a turn"
    )
class KeepBreathing(Rule):
    extra_effects = (
        "At the start of your turn,\n"
        "gain focus and stamina from your state:<hr>"
    ) + "<hr>".join(s.get_description() for s in Card.stances.values())
class YourHealth(Rule):
    extra_effects = (
        "Place a d6 to keep track of each of your statuses.\n"
        "They cannot go above 6.\n"
        "If they ever go below 1, draw the loss card to see how the fight ends"
    )
class ZZTest(Rule):
    your_requirements = [
        "smash a foot into their neck",
        ">2 oxygen",
        ">3 oxygen",
        ">4 oxygen",
        ">5 oxygen",

        "<3 focus",
        "<4 focus",
        "<5 focus",
        "<6 stamina",
    ]

class Loss(Card, ABC):
    # Flip over and read when you loose the game
    flavor_text = ""
class OxygenLoss(Loss):
    extra_effects = ("""
The muscles in your neck tense,
and churn, your diaphragm writhes.
Your face feels hot, pink,
and saliva is pooling by your esophagus.

Satisfaction seems an alien planet.
Struggling resignation feels like home.

You mouth chews dumbly. A tingle rises
along the inside of each arm,
a gray vignette pulls at the edge of your vision,
both growing with each
thump of your haggard heart.

A moment of dizziness bowls you over
- perhaps you crash to the ground, but of that, you are unaware.
All that remains is the fuzzy grayness,
and even that is descending away from you.

Your vision is a tight, milky cone.
And then it is gone.
""")

class BloodLoss(Loss):
    extra_effects = ("""
Looking down, your vision blurs
into a wet mess of red.

The blood streams in rivulets
down your body, it sloshes in your shoes.

Your little engine heart flutters and kicks,
and with each frightened beat,
your breath quickens.

The target pool of blood grows around you
it thickens, and darkens in the raw air.
A steaming, iron smell rises.
But you notice none of this.

You do notice the terrible chill
of your hind-brain gasping in horror.
Its psychic-scream is cut short.

Meekly, you touch a cold finger
to your salty, pale lips
as the color begins to drain from the world.

And you collapse.
""")

class PainLoss(Loss):
    extra_effects = ("""
You try to stand back, to push away,
but the anguish drags you to your knees.

Hot-pink and neon-green lightning
races through your neurons.
The feeling is white-hot.
Your mind is burning.

Involuntarily, your nails bite into your palm,
and your jaw is iron.
You think you feel a tooth crack,
but any pain is silent in the chorus.

You try to scream, but a wave of nausea
rises from your loins, and chokes you.

Suddenly, the world comes into a
sharp, gray relief, every vein dilating.

The vasovagal syncope claws into your mind,
pushing you out, dragging you
into the welcome release of the dark tunnel.
""")

class SensationLoss(Loss):
    extra_effects = ("""
Your eyes snap shut, but the comforting
dark behind your eyelids is missing.
There you find an alarming static,
an intense white-noise.

A fever-pitch ring rises in your ears,
drowning out the world completely.

"I can't..." you mouth, to no one. "I can't!"

Only cruel gravity and gritty palms tell
you you are crawling.
Your hand sweeps dumbly in-front of you, frantic
- what are you searching for?

Then, a swift kick plows into your sternum,
driving the wind out of you.
Your lungs click and gape as you fall
on your side, curling.

In a tight fetal position,
you don't hear their quieting footsteps,
you don't see their smug silhouette walking away.

You sense nothing.
You are alone.
""")

class FocusLoss(Loss):
    extra_effects = ("""
Your jaw slackens, fists loosen, and eyes swim.
Your purpled lips droop into an ischemic smirk.

Suddenly, a fist appears, teleporting hard
into your soft flesh. Then another.
Pain does not emanate from the blows,
but numbness. And confusion.

Great bruises bloom like hungry wildflowers.
How did those get there?

You move sharply, as if to block,
but only serve to collide your
elbow bone and hip. Whoops.

Deep in your mind a referee stamps,
and blows his whistle hoarse.
But the alarm is smothered by a
child-cloud that envelopes you.

How did I get here? The white noise is warm.

It will be a while until you recognize
they are calling your name.

It will be longer until you recognize
the battered face in the mirror.
""")

class RageLoss(Loss):
    extra_effects = ("""
The fire overran within you,
burned up everything inside you,
and filled you with an oily, choking smoke.

And then it snuffed itself out.

One second, you're clenched red,
blood thudding, beating your eardrums.

Now that feels like a million years ago.
The blows continue to land. And you feel them,
their just landing on a body that is no longer yours.

There is a pink quivering in your stomach,
a wet fish on the pier.
It flops on, but it knows that it is done.

You bring a hand to your belly.
The touch is wooden.

You are the dead horse, thoroughly beaten.
They are the cicada sun overhead.
But the heat of their anger begin to cool,
to back off. Shade returns.

And so here you sit, drained.
Numerous aches wait to paddle you tomorrow.
But for now you flop uselessly on.
""")

class DignityLoss(Loss):
    extra_effects = ("""
Inside you rings the sound of snapping chains.
With one hand, you grope and claw,
with the other, you throw a rhythmic fury of blows.
Teeth gnaw, ribid lips pull and curl.
Blood spatters into your eye,
momentarily waking you from your animalism.
Blinking, you peer down to survey your enemy,
and see one thing:

A look of steel defiance.

You pull back, eyes darting,
head snapping, hairs on your nape erect.
A distant siren rings in you mind
like the gong of the apocalypse.

What are you doing?!
You fucked up. You fucked up BIG.

You break off into a crouching run,
shoes squeaking, heart in a fluttery panic.

You have a while until the regret sets in.
But you already feel its weight above you
like a great thundercloud,
opaque as wine-colored velvet.
""")

class StaminaLoss(Loss):
    extra_effects = ("""
You scramble backwards,
landing on your arse,
kicking futilely to gain some distance.

Your breath is hot and forceful,
flapping your dry lips.
Your shoulders ache, and the pain
is mirrored in the hollow of your heart.

You try to form some resolute words,
but your ragged breath keeps cutting through.

Weakly, you raise a palm,
as if blocking your eyes from the light.
Weakness drags you down,
the heavy cords of gravity
anchoring you to the asphalt.

Your dull lead gaze returns to the
spittle spattered pavement before you.
You heavy breathing rocks you gently,
and the lullaby of you foamy gasps
cradles you to sleep.
""")

"""
TODO I'd like to do another set of loss:
focus = panic attack
stamina = vomiting
sensation = blissful lower-consciousness. Memory?
rage = masochism
oxygen = get high
dignity = disgust in yourself, cowardice
"""


# Card ideas:
"""
Feint
Thumb-eye Press Both grasp hands touch face     -1 dignity

Limb Control
Slap Away   Flat palm smack their limb          You can move that limb anywhere
Power Grip  Both grasp hands touch their wrist

Look over fighting moves, just add a bunch


Movement
Jump    Crouching       "-2 stamina
-1 rage
+1 dignity
For this turn, you can move"


Taunt - raise their rage. If high enough, they 'red out' and...
focus drops to 2?
...
"""

# Unused flavor text:
"""
...
"""

"""
Your head tips back, then rushes
at the opportunity to lie back.
You have no say in the matter


Laying on your side, you look up
for a moment at the silhouette
towering over you.
You can't see their face,
but you feel the pity and disgust nonetheless.
"""
