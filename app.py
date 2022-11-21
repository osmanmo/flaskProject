import random

from flask import Flask, render_template, request, flash
from wtforms import RadioField, SubmitField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
bootstrap = Bootstrap(app)


# make a rock paper scissors form
class RPSForm(FlaskForm):
    #     create a rock button
    rock = SubmitField('Rock')
    #     create a paper button
    paper = SubmitField('Paper')
    #     create a scissors button
    scissors = SubmitField('Scissors')


@app.route('/', methods=['GET', 'POST'])
def index():
    # create a form
    form = RPSForm()

    if form.validate_on_submit():
        # get the user choice
        # find if the user chose rock, paper, or scissors
        if form.rock.data:
            user_choice = 'rock'
        elif form.paper.data:
            user_choice = 'paper'
        else:
            user_choice = 'scissors'
        # get the computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        # determine the winner
        winner = determine_winner(user_choice, computer_choice)
        # return the results
        flash(f'You chose {user_choice} and the computer chose {computer_choice}. The winner is {winner}', 'success')
    return render_template('index.html', form=form)


def determine_winner(user_choice, computer_choice):
    winning_combinations = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    if user_choice == computer_choice:
        return 'tie'
    elif winning_combinations[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'


if __name__ == '__main__':
    app.run(debug=True)
