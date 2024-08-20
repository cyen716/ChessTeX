import chessTeX as TeX

_ = TeX.Throw_stuff_onto_the_pdf()

_.begin_pdf()

#Game 1 Corzo-Capa

_.mainline('P-K4 P-K4 N-QB3 N-QB3 P-B4')

_.comment(('Corzo knew my complete lack of opening knowledge, consequently he tried'
           ' repeatedly to find gambits of this sort where it would be difficult for me to find the proper answer.'))

_.mainline('PxP N-B3 P-KN4 P-KR4 P-N5 N-KN5 P-KR3 NxP KxN P-Q4 P-Q4')

_.comment('Afterwards Corzo told me that the book recommended $P-Q3$.')

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

_.mainline('{Resigns.}')

_.end_pdf('Game 1 Corzo-Capa')




