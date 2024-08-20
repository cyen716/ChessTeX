import chessTeX as TeX

_ = TeX.Throw_stuff_onto_the_pdf()

B='B'

_.begin_pdf()

# Game 7 Marshall-Capa

_.new_game()

_.comment('Game 7')

_.mainline(('P-Q4 P-Q4 P-QB4 P-K3 N-QB3 N-KB3 B-N5 B-K2 P-K3 N-K5'))

_.comment(('Today, when I have developed theories in accordance with my greater experience and knowledge, '
           'the chances are great against my making such a move, but then it was different, I did not know what to play,'
           ' and when someomne told me that Lasker had successfully played this move in his match with Marshall, '
           'I decided to adopt it. It was not till the end of the match, when I learned something else, '
           'that I changed my defence.'))

_.mainline('BXB QXB B-Q3')

_.comment(('The continuation adopted by Marshall in this game is in my opinion deficient.'
           ' I believe that he played this variation best in the twenty-first game.'
           ' Here, at any rate, I think it is best to play cxd5, followed by Qb3, after the knights have been traded.'))

_.mainline('NXN PXN N-Q2')

_.comment('$PXP$ is better.',B)

_.mainline('N-B3 Castles Q-B2 P-KR3 Castles_K')

_.comment('He still had time to play $PxP$, which was the correct continuation.', B)

_.mainline('P-QB4')

_.comment('With the idea of counterbalancing on the queenside the attack of White against the Black King.')

_.mainline('KR-K QPXP BXP P-QN3 Q-K4')

_.comment(('I do not think well of this manouver, as the attack is too slow to obtain any advantage, '
           'and on the other hand it compels Black to post his pieces where he wanted, i.e. the Bishop at b7, '
           'the Knight at f6 and his two Rooks at c8 and d8 respectively, thereby holding the open lines '
           'with the Rooks and ready at the same time to attack the enemy\'s center.'))

_.mainline('QR-N B-Q3 N-B3 Q-B4')

_.comment('If $Q-R4 {,  } N-Q4$ would have been sufficient.',B)

_.mainline('B-N2 P-K4 KR-Q QR-Q QR-B')

_.comment(('Black has now the surperior game, as there is no weak point in his position, and his queenside '
           'is much stronger than White\'s. Besides, the strategical position of Black\'s pieces is superior'
           ' to that of White\'s'))

_.mainline('R-K3')

_.comment('Not good, as Black quickly demonstrates. $B-N$ was the correct move.', B)

_.mainline('PXP PXP R-B6 B-N')

_.comment('An error, $Q-R4$ was the only chance White had of holding the game.',B)

_.mainline('P-KN4')

_.diagram(orientation=0)

_.mainline('NXP')

_.comment(('$Q-N3$ would have lost a pawn, but White sees chances of attack by sacrificing the knight and'
           ' consequently adopts this continuation in preference to the other, which he thought would also have lost the'
           ' game with less chances of a possible mistake on Black\'s part.'),B)

_.mainline('RXR QXR N-N5')

_.comment('$PxN$ would have avoided complications but would have left White with two pawns for the knight.',B)

_.mainline('Q-N3 QXN P-KR4')

_.comment('Had White played $Q-B7 {at once, Black would have answered } R-QB QXB R-B8 Q-N8 K-N2 R-B Q-Q7$ winning outright.',B)

_.mainline('Q-N2 Q-B7')

_.diagram(orientation=0)

_.mainline('RXP')

_.comment(('Not the best, as $Q-B3$ was the best move. Incidentally it would have saved me a great deal of'
           ' trouble which I had to win the game. Here I will call attention to the poor notes sometimes written'
           ' by analysts. Games are often annotated by unknown players who have not sufficient knowledge of the game.'
           ' As a matter of fact, the games of the great masters, at least, can only be properly annotated by very few'
           ' players. Of course even the best are not exempt from mistakes, but while they make them few and far in'
           ' between the others do so continuously.'),B)

_.comment(('I was highly praised by many because of the excellence of my play in this position,'
           ' while in reality I would have done better. They simply did not see that here $Q-B3$ was better'
           ' than the text move.'),B)

_.mainline('Q-N8 K-R2 P-K5 B-K5 RXR BXB QXRP NXKP R-KB4 B-K5')

_.comment('White should not have allowed this move.')

_.mainline('P-N3 N-B6')

_.comment('Very poor play, $P-B4$ at once was the right move. After the text move Black has a difficult game to win.',B)

_.mainline('K-N2 P-B4 QXP NXP K-R2')

_.comment('If $K-R3 {, then } Q-R8$ would win at once.',B)

_.mainline('N-B6 RXN')

_.comment("Forced, as Black threatened ...Ng5+ followed by ...Qh8.")

_.mainline('BXR QXP B-K5 P-B3 B-Q6 Q-Q5 Q-N7 K-N B-N8')

_.comment('It is from now on that it can be said that I played well. The ending is worth studying.')

_.mainline(('P-R4 Q-R8 Q-N7 K-N3 Q-N6 K-R4 K-R2 B-R7 Q-N5 K-N3 P-R5 Q-Q5 Q-B6 Q-B3 Q-K8 Q-B2 '
            'Q-R4 Q-K3 P-R6 Q-K7 K-R3 B-Q4 P-R7 BXP'))

_.comment('White resigns.')

#Game 8 Capa-Marshall

_.new_game()

_.comment('Game 8')

_.mainline('P-K4 P-K4 N-KB3 N-QB3 B-N5 P-Q3 P-QB3')

_.comment(('Not in accord with the true theory of the game, but as I have already said, my knowledge of such things'
           ' at the time was not of any account. $P-Q4$ is generally conceded to be the proper continuation.'),B)

_.mainline('B-N5')

_.comment(('I do not like this move, because later on the Bishop will be driven back by h2-h3 with evident gain of '
           'time for White. $P-B4$ seems good and leads to interesting complications.'),B)

_.mainline(('P-Q3 B-K2 QN-Q2 N-B3 Castles Castles R-K P-KR3'))

_.comment(('The manouver intended by Black is too slow to be good. Time is too important to be thus wasted.'
           ' White with the move possesses an advantage, which can only be held in check by very'
           ' accurate play on the part of Black.'))

_.mainline('N-B N-R2 N-K3 B-R4')

_.comment(('If $P-B4 PXP BXP NXB RXN P-Q4 {and White should win, because if } PXP <B-B3 B-Q3 > BXN$ followed by capturing '
          'with the knight wins a least a pawn.'),B)

_.mainline('P-KN4 B-N3 N-B5 P-KR4')

_.comment(('Not good, because Black can derive no advantage from the open h-file, while White will be able to utilize'\
          'it for his rooks. Better would have been $N-N4$ in order to simplify the position.'),B)

_.mainline('P-KR3 PXP PXP B-N4')

_.comment('I would have preferred $N-N4$, although the chances are that the position cannot be saved.',B)

_.mainline("NXB NXN K-N2 P-Q4 Q-K2 R-K R-R")

_.comment('Now what I said in a previous note becomes evident.')

_.mainline("R-K3 Q-K3")

_.comment(('a very important move, the object of which is to shut off the action of the opposing Queen and at the same time'
           ' to bring the White queen into the game. It also creates a weak diagonal in Black\'s game, '
           'against which the White bishop can act.'))

_.mainline('P-B3 B-R4 N-K2 B-N3 P-B3 Q-N3 P-R4 P-R4 N-B2 B-K3 P-N3')

_.comment(('To prevent the coming of the bishop to c5. It favors, however, the plan of White,'
           ' which is to close in the Black pieces so as to be able to use his own freely.'))

_.mainline('R-R4 K-B QR-KR N-N')

_.diagram(orientation=0)

_.mainline('Q-B3')

_.comment('Compelling Black to take the knight, strengthening still more the position of White.')

_.mainline('BXN NPXB R-Q3 Q-R5 R-R2 Q-N6 N(B2)-R3')

_.diagram(orientation=0)

_.comment(('There was no defense available. If $N-K2 R-R8 NXR RXN N-N Q-R7 K-B2 BXP$ winning.'),B)

_.mainline(('RXN PXR BXP K-K2 Q-R7 K-K QXN K-Q2 Q-R7 Q-K2 B-B8 QXQ RXQ K-K RXR'))

_.comment('Black Resigns.')

_.comment(('Outside of the opening it would be difficult to find where White could have improved '
           'his play. This is one of my best games. I saw Napier the day after I played it and he praised it highly.'))

_.end_pdf('Capa My Chess Career Chapter 4')