STARTWORD = '<S>'
STOPWORD = '<\\S>'

TEXT = [
'<S> you remember in the beginning <\\S>',
'<S> in the beginning god made man <\\S>',
'<S> god made man in his own image <\\S>',
'<S> and then that s was it <\\S>',
'<S>  man kind hu man ity wo man <\\S>',
'<S> man man man <\\S>',
'<S> what chance in hell did we ever have <\\S>',
'<S> we were sidelined from the big bang <\\S>',
'<S> you remember draupadi <\\S>',
'<S> draupadi married off to all five pandavas <\\S>',
'<S> she garlanded only arjun but they told her you got to marry all of us <\\S>',
'<S> five husbands that can t be fun <\\S>',
'<S> god know i have enough trouble with one <\\S>',
'<S> or what about eve and the apple <\\S>',
'<S> blaming one woman for all mankind s evil <\\S>',
'<S> soorya and kunti the virgin mary do you know gaia <\\S>',
'<S> the goddess mother earth she s the one we all trample on <\\S>',
'<S> and remember aphrodite goddess of love and beauty lest we forget she was also the patron of prostituting <\\S>',
'<S> persephone she was less known raped by hades she became queen of the underworld not even goddesses were left alone <\\S>',
'<S> you might not know a isha she was one of the wives of prophet mohammad she challenged a califh for power it created quite a ruckus it led to war in fact all because of one woman s fuss and so was born the tradition islamic that women should not engage in anything politic <\\S>',
'<S> but of course they did thank god they did <\\S>',
'<S> women have their ways as somebody once put it <\\S>',
'<S> the queen of sheba empress theodora rabia al basra cleopatra the victorian era the mona lisa the suffragettes marilyn monroe the sixties and burning bras the unpopular thatcher and our own indira et cetra et cetra and now here we are <\\S>',
'<S> here we are we ve survived this far thanks to seduction perhaps some manipulation but mostly thanks to mother nature and ovulation <\\S>',
'<S> now look at all the queens and goddesses of history no prince came to the rescue no king ever went down on one knee no deity was even that trustworthy yet all we ve be told since we were three are fairytales adverts and pretty stories telling us to pray hope and wait to be saved <\\S>',
'<S> here we are today <\\S>',
'<S> here we are on international women s day with some minor disappointments and a few little things to say <\\S>',
'<S> the woman in red the girl in pink the widow in white the burqa in black the colour of lipstick viva glam lady danger fresh brew faux frenzy hot gossip and sweetie <\\S>',
'<S> ramblin siss cr me cup paramount and modesty fetish spice it up naked paris honey love and odyssey <\\S>',
'<S> apply line smack seal pout and you re ready to go out <\\S>',
'<S> ugh sometimes i just want an oversized t shirt boxer shorts unkempt hair and unibrows <\\S>',
'<S> i want armpit hair long enough to plait i want a clean face without a trace of make up i want to look the way i do when i wake up <\\S>',
'<S> i want to scratch my head dig my nose lick my fingers stretch my legs and spread my toes <\\S>',
'<S> i want to smile with my gums showing bare my teeth and contort my pretty face into wrinkles <\\S>',
'<S> i want my crow s feet to look sexy or my salt and pepper hair or my sun burnt skin i want to be george clooney basically but with breasts and a muffin <\\S>',
'<S> control control keep it down <\\S>',
'<S> stuff it up bottle it in switch it off cross your legs wear a bra sit straight and smile sweetly for the camera <\\S>',
'<S> i went to a party i went to a party where i was looking for something real <\\S>',
'<S> glittering flashing lights sparkling clean glasses with something bubbly and expensive inside stuck on smiles of painted lips and gorgeous skinny beautiful ladies all around i craved a touch a caress but my senses were intimidated by cloned perfection <\\S>',
'<S> i thought i could hear muffled wailing nervous giggling intoxicated complying <\\S>',
'<S> i thought i could hear the buzz of millions screaming out their instructions sit down stand up stay this way that way go away i can t breathe i m choking <\\S>',
'<S> this room is filled with smoke from regrets and weak nicely packaged cigarettes <\\S>',
'<S> this room is filled with luxury and fame and false dreams <\\S>',
'<S> this room is full of fat sharks with sharp teeth sliding through delicate skin like a hot knife through butter <\\S>',
'<S> god i m so hungry <\\S>',
'<S> there s nothing to eat <\\S>',
'<S> no food except some frozen bits of fish on a silver platter i eat one <\\S>',
'<S> i m still hungry <\\S>',
'<S> i eat another and i m stared at by the waiter <\\S>',
'<S> i take the whole platter totter off to my little corner next to an old and and eat from my platter <\\S>',
'<S> i m stared at by the latter <\\S>',
'<S> i continue to eat from my platter <\\S>',
'<S> i wipe clean the crumbs from my platter <\\S>',
'<S> i lick clean the whole platter <\\S>',
'<S> what are you looking at <\\S>',
'<S> stop looking at me like that <\\S>',
'<S> i was hungry <\\S>',
'<S> haven t you ever seen somebody eat before <\\S>',
'<S> seriously stop staring at me <\\S>',
'<S> hey i m talking to you are you deaf <\\S>',
'<S> stop staring at me stop it <\\S>',
'<S> you ll drive me crazy oh god i m dizzy <\\S>',
'<S> it s that bubbly stuff they gave me this is one hell of a party <\\S>',
'<S> i have to leave <\\S>',
'<S> i m spinning and bumping into people and furniture i m spinning and bumping into everything <\\S>',
'<S> bumping into shiny lies through living ghosts past sickness ramming right into anger into wastefulness nothingness bad times endless sleepless nights half dead daylights violent bumps from losing loved ones losing innocence losing dignity losing looks losing just losing <\\S>',
'<S> i m craving i m starving for something real something breakable something tangled fragile imperfect and free <\\S>',
'<S> i am starving to be me <\\S>',
'<S> what am i complaining about <\\S>',
'<S> what right do i have to complain <\\S>',
'<S> i have money friends and fame <\\S>',
'<S> i m not fifteen and married i m not a little girl who s been lied to that she s a woman who s been told not to question a stranger who shares her bed i m not a little girl who s been raped before she s been kissed who s been made mother before she s had time to play does she even ask to be free <\\S>',
'<S> does she dream <\\S>',
'<S> when her husband enters her is it shah rukh khan she tries to see <\\S>',
'<S> does she feel sexy <\\S>',
'<S> i don t think so <\\S>',
'<S> this is her job twenty four hours seven days a week zero pay just get through each day <\\S>',
'<S> do you think she cares freedom rights about politics or religion she s fifteen <\\S>',
'<S> she cares about food and what her neighbors say <\\S>',
'<S> politics and religion are for the luckier the wealthier the stronger and in our country politics and religion are enviable careers <\\S>',
'<S> so your religion tells you to cover up your religion tells you to shave your head your religion tells you to be meek keep your eyes lowered keep having children or keep your mouth closed <\\S>',
'<S> what if your religion told you to hate the other what if your religion told you to burn alive on a funeralpyre what if your religion told you to do whatever you felt like spit scream gossip fight lose control make noise pollute marry a child perform an honour killing rape torture discriminate keep breaking the law keep locked up keep uneducated keep submissive keep ignored keep under control <\\S>',
'<S> does god have a say in your religion <\\S>',
'<S> has god become a politician <\\S>',
'<S> dear men dear powerful men i know you care about women <\\S>',
'<S> i know you care about her <\\S>',
'<S> i know you want her to feel like a princess i know you want to put her up on a pedestal make her a goddess and give her a special day international women s day <\\S>',
'<S> you want to carry her so she can t walk hold her so she can t be free tell her so she can t know any differently <\\S>',
'<S> but no no <\\S>',
'<S> that s not how works equality <\\S>',
'<S> it s hard work to change a nation s mentality it s hard work to go unnoticed change the roots and the minds of a people who have been too long deprived of education and basic rights who are steering towards intolerance and misanthropy because of shameless inequality <\\S>',
'<S> dear men in all this will you give me the power <\\S>',
'<S> will you let me stand in your place <\\S>',
'<S> will you let me laugh in your face <\\S>',
'<S> will you stop staring judging and accusing me or will you arrest me for blasphemy <\\S>',
'<S> label me as sexy slutty lose or crazy <\\S>',
'<S> call me basanti pinky sweetie and whistle at me <\\S>',
'<S> and wait a minute wait a minute not just dear men dear auntie will you stop gawking at me <\\S>',
'<S> dear didi will you stop telling me to shut up <\\S>',
'<S> dear ma will you stop ignoring me <\\S>',
'<S> dear women will you at least stand up for me <\\S>',
'<S> enough of a woman who has become viscous from her environment <\\S>',
'<S> enough of a woman who has to become a man to compete <\\S>',
'<S> who has to weaken where she is strong and strengthen where she is weak <\\S>',
'<S> enough of a woman that has to make space for child and lover that has to occupy what space is left over enough of uninformed teenage girls bleeding after losing their virginity and keeping silent after enough of having to deal all alone with the morning after enough of the disposed foetus enough of the unwanted daughter <\\S>',
'<S> enough of girls in fairy dresses with bulimia and major complexes enough of parents in denial gender gaps and dividing sexes <\\S>',
'<S> i m tired <\\S>',
'<S> you re tired <\\S>',
'<S> we are all tired <\\S>',
'<S> we re tired of waxing manicuring excercising aborting procreating trimming posing smiling threading shopping fucking water bursting the pill make up high heels stainless steels tampons covering up nurturing caring and crying <\\S>',
'<S> sometimes i just want to breathe sometimes it s hard to even just breathe <\\S>',
'<S> like when a man is pounding incessantly on top of you in a daily routine it s hard to breathe when he turns away to sleep leaving you completely unsatisfied sexually it s hard to breathe when your clothes are too tight the underwire of your bra is poking into your ribs it s too hot to be wearing all this and it s hard to breathe when you want to stop being stared at but everyone always is <\\S>',
'<S> the watchman the rickshaw wallah your neighbour s husband they re all watching your chest heave everytime you breathe <\\S>',
'<S> sometimes as a woman you feel guilty to just breathe <\\S>',
'<S> of course we are going to be hysterical of course we are going to scream of course we re going to be unreasonable <\\S>',
'<S> you think it s reasonable to restrain somebody s breathing <\\S>',
'<S> i am a hindu a muslim a christian a buddhist and an atheist <\\S>',
'<S> i am twenty thirty forty and fifty <\\S>',
'<S> i am single married divorced and half the country <\\S>',
'<S> i am a mother a daughter a wife and a prostitute <\\S>',
'<S> i am a stereotype a trophy and a prisoner or patriarchy <\\S>',
'<S> i am a woman in indian society and i am not yet free <\\S>',
'<S> but forget about all that for a moment and just look at me <\\S>',
'<S> look beyond my body really look at me <\\S>',
'<S> i am not a hardcore feminist to be very honest <\\S>',
'<S> i am not a rebel as some would like to believe <\\S>',
'<S> i am not even such an impressive celebrity i am not always made up and dressed up perfectly <\\S>',
'<S> and my therapist assures me that i m not crazy <\\S>',
'<S> so look beyond all that <\\S>',
'<S> look at me <\\S>',
'<S> look at what you re seeing <\\S>',
'<S> you re seeing another human being <\\S>',
'<S> you re seeing another you in me and really there is no difference between you and me <\\S>',
'<S> that s all we need to grow up understanding to make ours a better society <\\S>',
]
