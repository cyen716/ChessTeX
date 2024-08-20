import chessTeX as TeX

_ = TeX.Throw_stuff_onto_the_pdf()

_.begin_pdf()

#Game 1 Corzo-Capa

_.new_game()

_.comment('Game 1')

_.mainline('P-K4 P-K4 N-QB3 N-QB3 P-B4')

_.comment(('Corzo knew my complete lack of opening knowledge, consequently he tried'
           ' repeatedly to find gambits of this sort where it would be difficult for me to find the proper answer.'))

_.mainline('PxP N-B3 P-KN4 P-KR4 P-N5 N-KN5 P-KR3 NxP KxN P-Q4 P-Q4')

_.comment('Afterwards Corzo told me that the book recommended $P-Q3$.','B')

_.mainline('PxP Q-K2')

_.comment(('We had played this variation in a previous game, and Corzo had answered $B-K2$ to this check. '
           'The game ended in a draw, but I should have won. Corzo analyzed the position and told someone'
           ' that he should have played $K-B2$. When I heard this I analyzed the situation myself and decided'
           ' to play it again, as I thought that Black should win with the continuation which I put into practice in this game.'), position=_.current_position)

_.mainline('K-B2 P-N6 K-N')

_.diagram(orientation=0)

_.mainline(('NxP QxN Q-B4 N-K2 Q-N3 QxQ RPxQ '#14
            'N-Q4 B-QB4 P-B3 R-R5 B-K2 BxN PxB RxQP P-N3 N-B3 '#19
            'B-N2 R-Q7 B-R5 NxB BxR P-B6 PxP N-B5 B-K5 R-N7 '
            'K-B R-B7 K-K N-Q6'))

_.comment('White Resigns.')

#Game 2 Capa-Corzo (The last game of the match)

_.new_game()

_.comment('Game 2')

_.mainline('P-Q4 P-Q4 N-KB3 P-QB4 P-K3 N-QB3 P-QN3 P-K3 B-N2 N-B3 QN-Q2 PxP PxP')

_.comment(('When I see this game to-day I feel surprised at the good general system of my opening moves.'
           ' I remember that I always played $P-Q4$ with White, because in that way Mr.Corzo could not take'
           ' such great advantage of my weakness in the opening. In this game I played very well so far.'),
           position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

_.mainline(('B-Q3 B-Q3 Castles Castles N-KR4 '
            'P-N3 P-B4 N-K5 N-B3 P-KB4 BxN BPxB N-KN5 Q-K2 Q-N3 N-B3 B-Q2 P-QR3'))

_.comment(('To prevent $N-N5$ and also prepare the advance of the Q side pawns.'
           ' Today I would have followed the identical plan.'),'B')
_.mainline(('K-R P-R3 N-R3 Q-B2 N-B2 K-N2 P-N4 P-KN4 N-K2 '#20
            'Q-K3 R-KN QR-K N-N3 PxP N-B5 K-R2 NxB QxN PxP'))

_.comment(('The play for position preparatory to an attack is one of the hardest taxes upon the mind of the master player.'
           'Today, very likely, I would have done better, but nevetheless, all things considered, I did very well, and now,'
           ' in the deciding moment, I conceived a very excellent combination.'))

_.mainline('P-B4 Q-K3')

_.comment('I thought he would make this move, although $Q-KR3$ would have given him a better chance.','B')

_.mainline('PxP QxP(Q4) P-K6 B-N4') #28

_.comment('It is evident that if $BxP {,} RxB$.','B')

_.diagram()

_.mainline('QxB')

_.comment(('Today, very likely, I would have simply have played $Q-Q2$ and won also, but at the time I could not '
           'resist the temptation of sacrificing the Queen. At any rate, the text move was the only continuation which I '
           'had in mind when I played 28. e6.'), 'B')

_.mainline('QxQ P-Q5 R-N2 PxN P-KR3')

_.comment(('$R-KB {would have been better. The game would have proceeded as follows: } N-Q4 QxQP {(best)} '
           'R-K8 QxBP RxR QxR NxP$ and White should win.'), 'B')

_.mainline(('N-Q4 QxR'))

_.comment(('Best. If $Q-Q2 NxP QxBP BxR K-R2 R-K7 {, winning the Queen as Black cannot play } QxP {on account of }'
           ' B-K5 K-N3 R-N7 K-R4 N-N3 K-R5 R-B4 PxR R-N4$.'),'B')

_.mainline(('RxQ RxP RxP RxR NxR K-R2 N-K7 R-KB K-N2 P-KR4 P-Q6 P-N5 PxP PxP B-K5 K-R3 '#40
            'P-Q7 R-Q N-N8 RxN B-B6 K-N3 P-Q8=Q RxQ BxR'))

_.comment(('The rest is easy. One remark I must make before closing that epoch of my career: considering'
           ' my age and little experience this game is quite remarkable, even the endgame was very well played by me.'))

_.mainline(('P-N4 K-B2 K-B4 K-K3 K-K4 K-Q3 K-Q4 K-B3 P-N6 B-R4 P-N7 B-B2 P-R4 '
            'P-N4 K-K5 B-N6 K-Q4 K-Q3 K-B3 B-N K-Q4 B-R2 K-B3 K-Q4 P-R5 K-K5 K-N3 K-Q5 K-R3 K-B5'))

_.comment('Black Resigns. If $K-B6 P-N8=Q BxQ$ is stalemate.', 'B')

_.end_pdf('Capa My Chess Career Chapter 2')