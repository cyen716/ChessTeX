import chessTeX as TeX

_ = TeX.Throw_stuff_onto_the_pdf()

B='B' #This is part of the preamble, makes calling the previous position easier

_.begin_pdf()

#Game 3 Raubitscheck-Capa

_.new_game()

_.comment('Game 3')

_.mainline('P-K4 P-K4 P-KB4 PxP N-KB3 P-KN4 B-B4 B-N2 P-KR4 P-KR3 P-Q4 N-QB3 P-B3 P-Q3 Castles Q-K2 Q-N3 N-Q PxP')

_.comment('In this way White gains a pawn, but permits Black to work up a terrific attack.')

_.mainline('PxP Q-N5 B-Q2 QxKNP B-KB3 QxP N-K3 BxN BxB P-K5 PxP NxP')

_.comment('$PxP$ would have been better.','B')

_.mainline('Castles N-R3 R-R5 Q-N3 BxN QxB R-Q4 Q-N7 R-N5 Q-R7 N-B3! Q-R8 R-Q! QxN QR-N!')

_.diagram()

_.mainline('R-B2')

_.comment('If $QxQ RxP K-R B-Q4$, and mate follows in a few moves.','B')

_.mainline('RxP(N7) K-B B-B5 NxB R-N8')

#Game 4 Capa-Raubitscheck

_.new_game()

_.comment('Game 4')

_.mainline(('P-K4 P-K4 N-KB3 N-QB3 B-N5 N-B3 Castles NxP P-Q4 P-Q4 NxP B-Q2 '
            'NxB QxN N-B3 P-B4 NxN BPxN P-QB4'))

_.comment(('If $Q-R5 P-N3 BxN PxQ BxQ KxB P-KB3 B-N2 P-B3 QR-K$ and the game is about even.'
           ' If $BxN PxB Q-R5 Q-B2 QxQ KxQ P-KB3 PxP RxP K-K3 B-N5 P-B4 R-K K-Q2 R-B7 K-B3$,'
           ' and White has a slight advantage.'),'B')

_.mainline('Castles B-N5 B-K2 BxB')

_.comment('If $PxP BxB PxN QxQP$ and the game is about even.','B')

_.mainline('QxB BxN PxB P-B5 Q-B3 Q-R4 K-N QR-B K-R P-QN4 R-QN P-QR3 KR-K Q-R6 R-K3 P-QR4')

_.comment('White sacrifices a pawn in order to start an attack.')

_.mainline('QxP')

_.comment('If $RxP R-N$ wins.','B')

_.mainline('P-N5 Q-B3 R-B2 PxP P-B6 P-N5 R-B5 Q-Q5 R-N5 R(K3)-K R-N7 Q-B4 P-R3 P-Q5 K-R2 P-Q6')

_.diagram(orientation=0)

_.mainline('R-QB QxKBP')

_.comment('Black\'s only chance was to play $Q-Q5 R-B4 Q-N3 RxQ RxR RXKP {(best) } RxR Q-B8 R-N QxP$,'
          ' and it would be a hard game to play.','B')

_.mainline('R-KB Q-Q5 R-B5 P-K6')

_.comment('Mate in three.')

#Game 5 Fox-Capa

_.new_game()

_.comment('Game 5')

_.mainline(('P-K4 P-K4 N-KB3 N-QB3 B-N5 N-B3 Castles B-K2 R-K P-Q3 P-Q4 PXP NXP B-Q2 '
            'N-QB3 Castles N(Q4)-K2 R-K N-N3 N-K4 BXB QXB P-B4 N-N3 N-B5 B-B Q-Q3 QR-Q'))

_.comment(('If $NXKP RXN QXN RXR QXQ RXB$, followed by recapturing the Queen, and White is a piece ahead.'),B)

_.mainline('B-Q2 P-Q4')

_.comment(('The beginning of a fine combination. If $PxP RxR RXR NXP$, and it looks as though White must lose a pawn.'))

_.mainline(('P-K5 B-B4 K-R N-N5 N-Q P-KB3!'))

_.diagram(orientation=0)

_.comment(('The crowning move in the combination. If $PXP NXP(B5) {wins, because if } N-K7 RXN PXR NXQ '
           'PXR=Q QXQ PXN Q-R5 P-KR3 Q-N6$, and mate in a few moves. And if instead of 20. Ne7+, White plays 20.Rxe8+'
           ', then 20. . . Rxe8 21. Qc3 Qxf5 22. Qxc5 Ne2 wins.'))

_.mainline('P-KR3 N-B7 NXN BXN R-K2 PXP RXB P-K5 N-R6 PXN Q-Q4 Q-N2 QXRP')

_.comment('A bad move. $B-B3$ would have given White a fighting chance.',B)

_.mainline(('QXP R-K P-Q5 P-B5 P-K6 R(B2)-K2 N-B5 B-B Q-N3 Q-R4 NXR Q-B4 K-R RXN Q-R3 '
            'Q-Q3 QXQ PXQ P-B4 P-N4 P-B5'))

_.comment('White Resigns.')

#Game 6: Capa-Messrs. Davidson and Ferguson

_.new_game()

_.comment("Game 6")

_.mainline(('P-K4 P-K4 N-KB3 N-QB3 B-N5 N-B3 Castles B-K2 R-K P-Q3 P-B3 Castles P-Q3 P-QR3 B-R4 P-QN4 B-B2 N-K QN-Q2 P-B4'))

_.comment('This move is not as good as it looks, as will soon be evident.')

_.mainline('B-N3 K-R B-Q5 B-Q2 PXP RXP')

_.diagram(orientation=0)

_.mainline('P-Q4')

_.comment(('This move is the key to the situation. If now $PXP BXN BXB NXP R-QB4 N-K6$, winning the exchange.'
           'If $B-B3 B-K4 R-B5 <R-R4 NxP > N-B R-N5 P-KR3$. Black\'s reply, therefore, seems best.'))

_.mainline(('N-B3 BXN BXB PXP BXN NXB PXP Q-B2 P-K5 N-N5 Q-K'))

_.comment(('$Q-Q4 {seems better. There would have followed: } NXKP R-K4 P-B3 NXN PXN B-B4 K-R QR-K B-B4 RXP RXR QXR QXQ RXQ '
           'BXP R-K7 P-QN4 B-K2 B-N3$'),B)

_.mainline('NXKP B-B4 B-B4!')

_.comment('The winning move, and the only way to keep the advantage.')

_.mainline(('NXN RXN Q-B2 B-K3 B-Q3 P-QR4 R-R4 P-KN3 Q-N3 PXP RXNP QR-R4 P-KR3 Q-B K-R2 '
            'R-R4 P-KR4 Q-Q K-N P-QB4 R-KB4 Q-Q3'))

_.comment(('Threatening c4-c5.'))

_.mainline('P-B4 R-QR5 Q-B3 P-QN4 Q-B PXP B-K2')

_.comment(('If $BXP R-B4 RXR BXB Q-K PXR Q-K8 K-N2 QXR Q-Q5 K-R2 '#40
           'QXP K-N Q-Q5 K-R2 Q-K4 K-R3 <P-N3 Q-N7 K-R3 QXR QXB Q-R8 > '
           'P-B5 Q-Q B-K7$ winning.'),position=B)

_.mainline(('R-B4 RXR BXR R-Q B-Q6 BXB Q-Q5 Q-B2 PXB'))

_.comment(('Black resigns.'))

_.end_pdf('Capa My Chess Career Chapter 3')