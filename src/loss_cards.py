from abc import ABC
from src.card import Card

class Loss(Card, ABC):
    # Flip over and read when you loose the game
    flavor_text = ""
    count = 2
    loss = ["test1", "test2"]

    @classmethod
    def get_description(cls):
        cls.loss.append(cls.loss.pop(0))
        return cls.loss[-1].strip()

class OxygenLoss(Loss):
    loss = ["""
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
""",
"""
Half you mind is here, on the bloodied concrete:
hunting for an opening, readying a vicious volley.

The other half floats in cool lake water,
peering up at tannin-stained sunlight.
Your lungs are kicking, swimming, trying to
push you up into the world of air.

But the dappled surface pulls farther away.
You are sinking.
Icy, alge-choked water floods into your cranium.

Your amygdala is only big enough for one thought:
Breathe, goddamn it, you need to breathe.
Breathe!
Breathe... goddah... you...
...

The paramedics would note your feet's
'unconscious reflexive plantar responses'.
At the lake, you would sink
your toes into course, clay-filed sand.
"""
]

class BloodLoss(Loss):
    loss = ["""
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
""",
"""
test
"""
]

class PainLoss(Loss):
    loss = ["""
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
""",
"""
crawling away in blind fear
"""
]

class SensationLoss(Loss):
    loss = ["""
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
""",
"""
blissful lower-consciousness. Memory?
"""
]

class FocusLoss(Loss):
    loss = ["""
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
""",
"""
panic attack
"""
]

class RageLoss(Loss):
    loss = ["""
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
""",
"""
Yes. Yes!

Each blow you deliver -and receive-
brings sharp, delectable notes of pain.
The skin-seams at your knuckles and elbow fray,
and begin to pull apart.
Red velvet curtains opening for the show.

You punch now not to subdue them, not to win
- but to feel the bone-rattling ache that travels
like storm surge through your metacarpal stones,
like vibrato strings up the bow of your forearm,
like pneumatic hammering through the humerus,
to the collarbone, to the gooseflesh
at the nape of your neck.

The blinding wrath transmogrifies within you,
a changeling hate - you don't hate them,
you've forgotten about them.
But you love to hate yourself.

Masochism molts within you.
When you are done, your smile will be
unrecognizable.
"""
]

class DignityLoss(Loss):
    loss = ["""
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
""",
"""
You raise a fist to eye level, shielding your face.

And there you see it:
the ugly split knuckle,
oozing thick blood-drops like fat leeches.
Sweat welling in fine, matted metacarpal hairs
like oil fires on a war-blasted desert.

Minutes ago you traded fine fingers
and pressed cuticles for these
despicable crooked digits and cracked nails.

What kind of worship leaves the temple this way?

You expectorate blood from your mouth,
and the spit lands upon your name.

Your honor crunches beneath you feet like glass.
The shards of your decency digging their way
into the dirty flesh of your sole.

A nausea grows slowly inside, not to be
soothed by soft food, nor expunged by retching.

It too, buries itself within your bruised body,
promising to painfully resurface each morning
when you look in the mirror.
"""
]

class StaminaLoss(Loss):
    loss = ["""
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
""",
"""
You try to lift your arms
- but all energy seems to drip out of them:
the 'chi' streaming like warm piss
down your pits, up your thighs,
collecting in a sickly stomach pool.

It sloshes nauseatingly. Your abs squirm:
contractions giving birth to a desperate collapse.

A wave of cold runs up your genitals,
washing over the whirlpool in your belly.

Acid burping drags razors along your esophagus,
and singes your nostril hairs.
You press your eyes shut, gird your teeth
- but you know it is too late.

The chain-retching threatens to knock your
adams-apple free. To tie your larynx in a knot.

You puke. And puke and puke.
You snap your head to and fro,
stupidly trying to point it somewhere.
But instead of somewhere it goes everywhere.

So yeah. Fight's over.
"""
]
