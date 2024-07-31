from abc import ABC
from src.card import Card

class classproperty(object):
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        return self.f(owner)

class Loss(Card, ABC):
    # Flip over and read when you loose the game
    flavor_text = ""

    @classproperty
    def count(self):
        return len(self.loss)

    loss = ["test1", "test2"]

    @classmethod
    def get_description(cls):
        cls.loss.append(cls.loss.pop(0))
        return cls.loss[-1].strip()

# TODO
# you know what? Lets give each of these 'fun' names
# for the medical or psychological or whatever
# So Oxygen Loss is the category, and Hypoxia is the card

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
Icy, algae-choked water floods into your cranium.

Your amygdala is only big enough for one thought:
Breathe, goddamn it, you need to breathe.
Breathe!
Breathe... goddah... you...
...

The paramedics would note your feet's
'unconscious reflexive plantar responses'.
At the lake, you would sink
your toes into course, clay-filed sand.
""",
"""
Sip each tiny breath, the burps of cool, teal air
finding their way to desperate, blackening lungs.
Your lips are witted with the anticipation,
Every breath is a poltergeist:
it brigs sensation, but is unable to be grasped.

The Norns are undoing the world,
pulling at the threads.
Sound is replaced with distant siren-song.
Reality softens, and frays.

You fumble, tumble,
your legs weakly informing you
that you must be standing on sand.

But no - there is the ground,
greeting you hard and sudden.
The bruising fall feels somehow muffled,
the asphalt like thick, warm velvet beneath you.

There is a last moment of lucidity, of panic,
of eyes-wide, leg-kicking, rabid-rabid fight.
It is quickly subsumed by the yawning void.
""",
"""
You hammer at your tight chest,
like a desperate miner, each breath a pickaxe.
Each straining pull brings no air, no relief
- only another sharp blow deep in your diaphragm.

The sweet sounds of the world are lost
to the squeal of grinding stone.
A sepia-gray is spilled onto your sight,
and tears well up in in your bottom eyelids
the colors of the world washing out in the rain.

Numbness emerges from the depths,
crawling like so many thousand black insects.
Up your leg, under your pants. Within you.
They mount a surrounding-siege of your brain.

They've taken your lungs. They riot in your nerves.
They are coming for your mind.

All you can do is <i> grip </i> your identity.
Sights and sounds dissapear beneath the
horde of tiny coal devils.
All you have is you.

You must hold off the darkness. You must.
"""
] # noqa

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
A drip, a cupful, a river.
Your warmth spilling sweetly
onto the cold, uncaring ground.

A scarlet gardener - wasteful and merry
using up your every drop of fallow land.

Your wild-drum heart keeps you standing,
keeps you clutching at your wounds,
but already you feel your grip start to slacken.

As blood leeks out through your pressed fingers,
so too does your consciousness leek out
of your failing grasp on reality.

You try to draw your mind away
from the red-gold spilling at you feet
- and back to the hand you've been dealt.
How do we play these cards,
and still wake up tomorrow?

But your vision has become a pinpoint,
and your body topples back in freefall.

Its not up to you any more.
Now its up to them.
""",
"""
Time begins to slow,
your frenzied fists freezing in place.

Your body aches,
like a spring coiled too tightly.
Your heartbeat races
as if straining to hold you together.

Then cold wind brings frost, and the chill
blows transparent through you.
One last straw, too much for your poor heart.

Its marching trot becomes a panicked gallop,
an arrhythmia sending staccato stabs of pain.

Your hand gropes at your chest, as if to
massage the blood back into your veins,
or squeeze a fresh batch from your marrow.

But a wave of exhaustion crashes into your mind,
you are tossed, bobbing in dark, choppy waters.

A rising panic becomes a tumbling resignation.
Tachycardia to Bradycardia.
Your 'will' draining out of you like all other fluids.
Before you plunge into the deep.
""",
"""
A droplet of sweat crawls down your spine.
It feels cold. Perspiration beads over you
like dew after the last summer day.

Where did all this <i> gore </i> come from?
Who's blood is this?

Red ink drips into your eye, contorting
your sight with circus visuals.
This viscera lavalamp causes you to stumble.
Was blood always this cartoonist bright?

An innocent sunlight radiates over you.
You breaths come in short, rabbit-like gasps.
Your wobbly steps are light,
your knees weak as a newborn fawn's.

"It's all going to be okay."
you think, as you buckle and collapse.
But all thoughts are gone
before you hit the ground.
"""
] # noqa

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
Okay, hold on. Blink. Cough. Unclench your jaw.
You got this.

But then another blow knocks stars into your eyes,
and spins you round,
palms landing on the gritty earth.

The warrior within wills you
to turn, to defend yourself,
to guard your face, to rear back for another -

No. No more.

Barley have the words echoed from ear to ear
before you are crawling
-no, pawing
-no, scrambling to get free.

To get away from them,
but to get farther away from yourself.
From the mangled body you choose,
when you choose violence.
""",
"""
The world blurs with long-exposure,
the agony sending your mind into overdrive.
Your forehead is hot with a hundred calculations,
with the 'fight' and 'flight' and 'freeze' brawling
up and down your spinal column.

'Fight' has held the throne until now.
But it has lost, and is tossed out.

'Freeze' holds you for a moment of serenity.

Then 'flight' grips the controls.

No thought drives you forward - but pain.
Pain, like a whip cracking on your sweaty back.
Pain, like a housefire radiating behind you.
Pain, searing this flashbulb memory-negative forever.

And whenever you taste adrenaline in the future,
you will live this pain again.
""",
"""
The battle started with words, shoves and sneers.
Then it became the artillery fire of punches,
the outmaneuvering and flanking on the ground.

And now, your battle just to stand upright.

Torment splashes at your legs,
the rising waters of suffering
sending ischemic twinges and throbs
up your hips.

It wallows around your belly, which locks tight.
Your body becoming a tomb as the rising waterlevel
brings spasms and clonic contractions.

The torture rises to your neckline, bringing lockjaw,
and as the 'nails' are being driven into your temples-

Lights out.
"""
] # noqa

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
The taste is familiar. Concentrated sweat.
The zinc flavor of adrenal,
and the iron of fresh blood.
A spoonful of parotid enzymes
(and a tingling sensation under the jaw).

There you are, on the side road.
Eight years old? Nine?
Dappled sunlight on your road-rash knees,
a crack in your helmet
<i>("oh thank god, you were wearing it!)</i>,
and a purpled lip for school pictures.

Mom is not far away - but she isn't here yet.
Its just you, and the pain, and the flavor,
and golden rays of sunlight.
Photons are born and die in the same instant.
And that was many years ago.

Do zinc and iron form an alloy?
I don't know if they do...

A million miles away,
your bruised body rolls on the pavement
a battered bunker, for a hideaway mind.
""",
"""
You head swirls and, unknowingly,
you swipe your gaze directly over the sun.

In the center of your vision, a technicolor smudge
grows and dances:
your cones raving to exhaustion,
your rods drowning in the noise.

The photopsia elongates and grows,
a searing white blindfold thrust upon you.
You snap your head to and fro, trying to
shake materiality back to sharp vision.
It doesn't work.

Your ears strain to rush you pertinent data
-it flows excessive, with scant context.
You can't make sense of anything.

Your hated opponent no longer exists,
and neither does the world
- swallowed equally by the white void.
""",
"""
<i>Where</i> is their other fist?
Are they drawing back for another kick??
Damn it! Don't loose track of them!

You brain buzzes with excess electricity,
as if arcs of plasma leap from your
cranium to graymatter,
blackening the neurons they touch.

Your psyche is stretched thin, worked, and folded,
like boardwalk taffy. Your vision warps and blurs.

Though it all, fear cuts like a hot knife.
It wills you to clarity.
It hacks, chops away at the confusion.

The terror is overzealous
in its need for your attention,
it is auto-immune, feverish.
The fright demolishes your last mental link
to terra firma.

Your eyes flutter, and you fall.
""",
] # noqa

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
Something is wrong.
Something is terribly, deathly wrong.
'You are going to die. You are dying. You are dead.'

Agony drills into your heart,
then shoots down your left arm,
as if driven home by twenty blasts
of a nail gun.

Your heart spikes the pressure,
a throbbing drums at your ears,
and squeezes tears from your eyes.

No more, please. No more.
'You are dying. You are dying.'

Part of you know it's not true -
bruised, yes, and you will ache tomorrow.
But that little voice
is engulfed by monochrome flame.

In a few hours, you will wonder what happened,
where it was that your mind went.

But right now, you are <i>there</i>.
Right now, you can never leave.
'You are going to die. You are dead.'
""",
"""
Okay, hold on. Just. Hold on.

Your mind reels, gripping itself tightly.
Thoughts orbit and crash into eachother,
Strategy, proprioception, and instinct
topple out of your reach,
and shatter on the floor of your skull.

'Keep it together.' part of you says.
'Fuck you.' responds the rest.

And with that declaration,
the fighting spirit within you deflates.
It rolls of the table, and explodes
into glittering shards.

Your reasoning becomes a madhouse highway:
idle-musings plow headlong into somatic-alarms,
egoistic-shame T-bones self-preservation.
A hundred perceptions, notions, and convictions
piled high into a burning pyre.

Who knows what's happening to your body now.
Who cares. You're done.
""",
"""
Panic rattles its cage.
You've kept it locked up so far,
but the warden is battered, and tired.
And the beast has only grown.

A moment of lost focus, an instant
and anxiety bursts through its enclosure,
shattering your thoughts as it does.
Roaring thunders in your ears,
and weakens your legs.
It drags its claws across the backs of your eyes.

You stood on the ledge too long,
looking down into the abyss.
Now your mind if tipping, teetering, toppling.
You cast a hand out: to courage, to rationality
- but they are not there.
Perhaps cajoling panic back into its cage.
Perhaps dead under its paw.

Derealization lies below,
the only thing waiting to catch you.
And so you close your eyes, and plummet.
""",
] # noqa

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
""",
"""
You hesitate. Then draw you fist back further.
Then hesitate again.

Are we still doing this?

You've wrung every drop of emotion from
your tattered, lusterless brain.
But your not angry anymore.
Your not disappointed.
Your exhausted. Empty.

A single drop of blood traces your frozen fist.
The dripping sound echos hollowly within you.

The inside of your chest feels sore and vacant.
Someone has scraped every mote of sweet flesh
from the dry, bony husk. That someone was you.

Inside your mind, some part of you lights a torch
to explore the cavernous gloom.
Outside, your face slackens,
taking the palor of dead fish.

A numbness flattens the worldly projection.
The vivid 3d falls to a faded storybook.
Already this waking moment feels
like a discarded memory.
""",
"""
Each thudding blow - yours and theirs -
they all served to harden your heart.
Inside you, a great dam holds back the
roiling sea of emotion.
Kaleidoscopic waters of a thousand emotions,
purple thunderclouds overhead.

Looking down, your eyes meet theirs.
Human connection. Oneness. Sonder. Ubuntu.

Like inverted lightning, a crack splits your
concrete heart.
There is a moment of silence within you.
And then cacophonous empathy
washes over the land.

Your eyes sparkle with fresh tears,
wellsprings cleaning the blood from your cheeks.
Fists unclench to a cradling hold.
Puppet-strings cut, and every muscle softness.

You melt.
""",
] # noqa

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
""",
"""
A dull ache in your fists preludes
a rising feeling of satisfaction.
But the aftertaste is... not as pleasant.

"This is why everyone despises you."
The thought lances through you.
"You're worthless. A waste."
Each word feels like a perforating bullet,
cold wind rushes into the wounds.

"They'll mock you for this. They'll deserve to."
Your ego reels, scanning your battered
opponent for evidence of your dominance.
But like Icarus, each self-sooth is followed
by a dizzying fall.

"The repercussions will <i>unmake you.</i>"
You take a step back.
"How can everyone bear to be burdened by you?"
You turn your face away, squinting.
"How much longer can you dare to burden them?"
Your tearducts tickle.
But the rain feels undeserved.

"And now you'll run. Like you always do."
""",
"""
That bastard. They'll pay.
Here we go, a clean opening
- your nails flash, and bicep flexes -
this is going to be <i>devastating</i>.
A sneering smile begins to spread
across your lips - but is halted.

Somewhere inside you,
a child tugs at your sleeve.

A stunned grunt leaps from your throat.
Of course, the youth has your face,
not bruised from combat,
uncontorted by time.

They don't say anything.
But their whole, tiny form <i>pleads.</i>

You can see their eyes,
as if level with your own.
Scleras unimaginably white.
Pupils unbearably dark.

Together, you cry.
""",
] # noqa

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
""",
"""
Your fingers clamp down,
wrist tucking inward against your will.
Toes curl, and a winching tightness
threatens to fold your calves.

Cramp. Cramp!

A corrosive, yellow pain twangs and twists
along each bundle of muscle fibers.
You feel as if lactic acid will dissolve your insides,
as if taunt tendons will snap your bones,
like an overworked crossbow.

Perhaps flexing will help...
Do you dare?

Of course you do, and the instant
shooting, searing, insufferable pain
debilitates you
with a swiftness no punch could match.

You writhe and yelp with a strange rhythm,
arms flapping, lips curling back.
Like a rusted piece of clockwork,
like a broken cymbal-banging monkey.

Eat a banana next time.
""",
"""
Your tongue flicks over dry, craggy lips.
A metallic glue coats the roof of your mouth,
a sagging drags at the bags of your eyes.

Your heart <i>had</i> been racing, but now each pound
comes slower, firmer, and less assured.
A slow locomotive on an rising slope,
a blacksmith falling asleep at the anvil.

The dizzy feeling makes you want to cry,
but your tearducts drink from your eye instead.
You skin feels blotchy, flushed, and cold,
you shake, as if trying to knock leaches free.

You can't fight like this.
It hurts enough just to stand!

Retreat, retreat,
return to the ocean.
Immerse yourself
in the warm womb of the earth.
""",
] # noqa

"""

A grunting whimper accompanies

Your head tips back, then rushes
at the opportunity to lie back.
You have no say in the matter

Cold dread seeps into your flesh,
penetrating your bones.
You've marinated in the frigid fear this whole fight.
But the focused heat of battle kept it at bay,
- until now.

Laying on your side, you look up
for a moment at the silhouette
towering over you.
You can't see their face,
but you feel the pity and disgust nonetheless.

You feel if you keep crying,
you will go blind.

"""
