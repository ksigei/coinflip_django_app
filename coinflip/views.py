
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from decimal import Decimal
import random



@login_required
def place_bet(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        bet_amount = Decimal(request.POST.get('bet_amount', '0.0'))

        if bet_amount > Decimal('0.0') and bet_amount <= user_profile.balance:
            # Deduct the bet amount from user's balance
            user_profile.balance -= bet_amount
            user_profile.save()

            # Simulate coin flip
            result = random.choice(['Heads', 'Tails'])

            # Calculate winnings based on the result
            if result == 'Heads':
                winnings = Decimal('2.0') * bet_amount  # User wins double the bet amount
            else:
                winnings = Decimal('0.0')  # User loses the bet

            # Add the winnings to the user's balance
            user_profile.balance += winnings
            user_profile.save()

            return redirect('results', result=result, winnings=winnings)

        else:
            return JsonResponse({'error': 'Invalid bet amount'})

    return render(request, 'place_bet.html', {'balance': user_profile.balance})

@login_required
def results(request, result, winnings):
    # Convert winnings to float
    winnings = float(winnings)
    return render(request, 'results.html', {'result': result, 'winnings': winnings})