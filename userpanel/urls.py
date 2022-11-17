from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = 'userpanel'

urlpatterns = [
    path('',views.indexpage, name = 'index'),
    path('dashboard',views.dashboard, name = 'dashboard'),
    path('register',views.register, name = 'register'),
    path('request_chips',views.request_chips, name = 'request_chips'),
    path('unused_codes',views.unused_codes, name = 'unused_codes'),
    path('used_codes',views.used_codes, name = 'used_codes'),
    path('obtain_earnings',views.obtain_earnings, name = 'obtain_earnings'),
    #path('',views.new_referral, name = 'new_referral'),
    path('my_referrals',views.my_referrals, name = 'my_referrals'),
    path('level_earnings',views.levelearning, name = 'level_earnings'),
    path('new_ticket',views.new_ticket, name = 'new_ticket'),
    path('all_tickets',views.all_tickets, name = 'all_tickets'),
    path('kyc',views.kyc, name = 'kyc'),
    path('playgame',views.playgame, name = 'playgame'),
    path('playgame3m',views.playgame3m, name = 'playgame3m'),
    path('playgame99',views.playgame99, name = 'playgame99'),
    #path('profile',views.Profile, name = 'profile'),
    #path('closing',views.closing, name = 'closing'),

    path('topup_account',views.topup_account, name = 'topup_account'),
    path('transfer_chips',views.transfer_chips, name = 'transfer_chips'),

    path('login',views.loginUser, name = 'loginUser'),
    path('logoutuser',views.logoutUser, name = 'logoutuser'),
    path('validate_username', views.validate_username, name='validate_username'),

    path('addnewlottery', views.addlotteryadmin),
    path('getlottery', views.getlottery),
    path('getresult', views.getresult),

    path('addnewlottery3m', views.addlotteryadmin3m),
    path('getlottery3m', views.getlottery3m),
    path('getresult3m', views.getresult3m),

    path('addnewlottery99', views.addlotteryadmin99),
    path('getlottery99', views.getlottery99),
    path('getresult99', views.getresult99),

    path('lotteryresult', views.lotteryresult, name="lotteryresult"),
    path('placebet', views.placebet),
    path('placebet99', views.placebet99),
    path('mybets', views.mybets, name="mybets"),
    path('result3m', views.result3m, name="result3m"),
    path('result15m', views.result15m, name="result15m"),
    path('result99', views.result99, name="result99"),
    path('wallet', views.wallet, name="wallet"),
    path('accounting', views.accounting, name="accounting"),
    path('add_distributor', views.add_distributor, name="add_distributor"),
    path('add_agent', views.add_agent, name="add_agent"),
    path('add_user_byagent', views.add_user_byagent, name="add_user_byagent"),
    path('add_user_from_panel', views.add_user_from_panel, name="add_user_from_panel"),
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)