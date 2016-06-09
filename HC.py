import numpy as np
import matplotlib.pyplot as plt

def expected_roll ( number_of_dice ):
    """
     This function computes probability of each possible 
     outcome when rolling n dice.
    
     by: Francesc Massanes, June 2016
    """
    
    pr = np.ones(6) / 6.0
    prob = pr

    for dice in range(2, number_of_dice + 1):
        prob = np.convolve(prob, pr)

    roll = np.arange(number_of_dice, number_of_dice * 6 + 1)

    return roll, prob

def roll_at_least( target, number_of_dice ):
    roll, prob = expected_roll ( number_of_dice );
 
    return np.sum( prob[roll>=target] );

def survive_options ( name, defense, armor, boxes, focus, hunters = 9 ):
    POW = 6;
    RAT = 7;
    armor = np.ceil(armor/2)
    hitting = roll_at_least( defense-(RAT+2), 3 );
    
    dice, prob = expected_roll( 2 );
    dice = -( armor - ( POW + dice ));

    D = {};
    for roll in range(dice.shape[0]):
        D[dice[roll]] = hitting * prob[roll];

    cumulative = { 0: 1 };
    
    for attacks in np.arange(0,hunters):
        tmp = {}
        for d1 in cumulative.keys():
            for d2 in D.keys():
                d = d1 + d2;
                if attacks < focus:
                    d -= 5;
                tmp[ d ] = tmp.get( d, 0.0 ) +  cumulative[d1] * D[d2]
        cumulative = tmp;

    odds = 0;
    for damage in cumulative.keys():
        if damage >= boxes:
            odds += cumulative[damage];
            
    return 'The odds of %s surviving are %.2f%%, so he/she is dead in %.2f%%' % (name, (1-odds) * 100, odds * 100 )
