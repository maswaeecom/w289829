from decimal import *
import decimal
from django.utils.html import format_html
from django.urls import path
from django.contrib import admin
from django.http import HttpResponse
from userpanel.models import Earning, Member, Coderequest, Epin, Rewards, newlotteriesthreem
from .models import *
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render
import datetime
from django.db.models import Sum, Max, Min
from django.contrib import messages
admin.site.unregister(Group)
admin.site.unregister(User)





def closing_view(request):
    
    if request.method=="POST":
        yes = request.POST.get('yes')
        if yes == 'yes':

           
            closeEarning()
            

            # messages.success(request, 'Dividend closing successfully')

        else:
            messages.error(request, 'Error in closing')
            print('Not OK')
    
    return render(request, 'closing.html')




def closeEarning():
    members = Member.objects.all()
    for m in members:
         total = Earning.objects.filter(userid = m.userid, status='Pending').aggregate(Sum('amount'))
         totalearn = total["amount__sum"]
         totalpending = 0 if totalearn is None else totalearn
         finalbalance = 0
         if totalpending > 0:
             
             try:
                  walletbalance = Wallet.objects.filter(userid=m.userid).values_list("balance", flat=True)
                  for bal in walletbalance:
                      finalbalance = float(totalpending) + float(bal)
             except: Wallet.DoesNotExist
             pass

             try:
                Wallet.objects.filter(userid = m.userid).update(balance = finalbalance)
                Earning.objects.filter(userid = m.userid).update(status = 'Paid')
                print(m.userid, totalpending, finalbalance)
                return True

             except:
                 pass


# def PayDividend():
#     members = Member.objects.all()
#     for m in members:
#          total = Dividend.objects.filter(userid = m.userid, status='Pending').aggregate(Sum('amount'))
#          totalearn = total["amount__sum"]
#          totalpending = 0 if totalearn is None else totalearn
#          finalbalance = 0
#          if totalpending > 0:
             
#              try:
#                   walletbalance = Wallet.objects.filter(userid=m.userid).values_list("balance", flat=True)
#                   for bal in walletbalance:
#                       finalbalance = float(totalpending) + float(bal)
#              except: Wallet.DoesNotExist
#              pass

#              try:
#                 Wallet.objects.filter(userid = m.userid).update(balance = finalbalance)
#                 Dividend.objects.filter(userid = m.userid).update(status = 'Paid')
#                 print(m.userid, totalpending, finalbalance)
#                 return True

#              except:
#                  pass

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'userid', 'email', 'phone' ,'username','join_date', 'sponsor', )
    # exclude = ('Action',)
    list_per_page = 100
    search_fields = ('userid',)

    # def Earning(self, obj):
    #     total = Earning.objects.filter(userid = obj.userid).aggregate(Sum('amount'))
    #     return total["amount__sum"]

    # def Dividend_paid(self, obj):
    #     total = Dividend.objects.filter(userid = obj.userid).aggregate(Sum('amount'))
    #     return total["amount__sum"]

    def Directs(self, obj):
        return Member.objects.filter(sponsor = obj.userid).count()
    
    def Wallet_balance(self, obj):
        wallet = Wallet.objects.filter(userid = obj.userid).get()
        return wallet.balance

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False


class EpinAdmin(admin.ModelAdmin):
    list_display = ('epin', 'amount','issue_to', 'generate_time', 'used_by', 'used_time', 'status')
    exclude = ('epin','Action','generated_by', 'used_by', 'used_time', 'status')
    list_per_page = 100
    search_fields = ('epin',)
    readonly_fields = ('epin',)
    
    



class RequestcodeAdmin(admin.ModelAdmin):
    list_display = ('username', 'hash','amount', 'date')
    exclude = ('Action',)
    list_per_page = 50
    search_fields = ('userid',)
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    



class EarningAdmin(admin.ModelAdmin):
    list_display = ('username', 'amount','type', 'levels', 'ref_id', 'date',)
    list_per_page = 100
    search_fields = ('userid',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False


class MprofileAdmin(admin.ModelAdmin):
    list_display = ('userid','id_proof_tag','add_proof_tag','photo_tag',)
    list_per_page = 100
    search_fields = ('photo',)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('username','balance',)
    list_per_page = 10
    search_fields = ('userid',)

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('userid','amount', 'status', 'paid_date', 'trans_detail')
    list_per_page = 10
    search_fields = ('userid',)
    list_filter = ('status',)

class KycAdmin(admin.ModelAdmin):
    list_display = ('userid','id_proof', 'address_proof', 'photo',)
    list_per_page = 100
    search_fields = ('userid',)

class DividendAdmin(admin.ModelAdmin):
    list_display = ('userid','amount','date','status',)
    list_per_page = 100
    exclude = ('Action',)
    search_fields = ('userid',)

    def has_delete_permission(self, request, obj=None):
       return True

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False











class Adminnewlotteriesthreem(admin.ModelAdmin):
    list_display = ('id','created_at', 'status', 'total_amount', 'min_number','Max_number', 'Result', 'all_amount')
    list_per_page = 10
    search_fields = ('period',)
    list_display_links = None


    def total_amount(self, obj):
        sum = BetSingle.objects.filter(period=obj.id, timing=3).aggregate(Sum('amount'))
        return sum['amount__sum']

    def all_amount(self, obj):
        betamount = {}
        for number in range(10):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=3).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        # smallnumber = min(betamount.values())
        # minvaluenumber = min(betamount, key=betamount.get)
        return betamount


    def min_number(self, obj):
        betamount = {}
        for number in range(10):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=3).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        smallnumber = min(betamount.values())
        minvaluenumber = min(betamount, key=betamount.get)
        return minvaluenumber

    def Max_number(self, obj):
        betamount = {}
        for number in range(10):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=3).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        smallnumber = min(betamount.values())
        maxvaluenumber = max(betamount, key=betamount.get)
        return maxvaluenumber

    

    def Result(self, obj):
        res = Resultthreem.objects.filter(period = obj.id).get()
        return res.result

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


class Adminnewlotteries15m(admin.ModelAdmin):
    list_display = ('id','created_at', 'status', 'total_amount', 'min_number','Max_number', 'Result', 'all_amount')
    list_per_page = 10
    search_fields = ('period',)
    # list_display_links = None


    def total_amount(self, obj):
        sum = BetSingle.objects.filter(period=obj.id, timing=15).aggregate(Sum('amount'))
        return sum['amount__sum']

    def all_amount(self, obj):
        betamount = {}
        for number in range(10):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=3).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        # smallnumber = min(betamount.values())
        # minvaluenumber = min(betamount, key=betamount.get)
        return betamount


    def min_number(self, obj):
        betamount = {}
        for number in range(10):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=15).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        smallnumber = min(betamount.values())
        minvaluenumber = min(betamount, key=betamount.get)
        return minvaluenumber

    def Max_number(self, obj):
        betamount = {}
        for number in range(10):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=15).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        smallnumber = min(betamount.values())
        maxvaluenumber = max(betamount, key=betamount.get)
        return maxvaluenumber

    

    def Result(self, obj):
        res = Result.objects.filter(period = obj.id).get()
        return res.result

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False



class Adminnewlotteriesnine(admin.ModelAdmin):
    list_display = ('id','created_at', 'status', 'total_amount', 'min_number','Max_number', 'Result')
    list_per_page = 10
    search_fields = ('period',)
    list_display_links = None


    def total_amount(self, obj):
        sum = BetSingle.objects.filter(period=obj.id, timing=10).aggregate(Sum('amount'))
        return sum['amount__sum']


    def min_number(self, obj):
        betamount = {}
        for number in range(99):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=10).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        smallnumber = min(betamount.values())
        minvaluenumber = min(betamount, key=betamount.get)
        return minvaluenumber

    def Max_number(self, obj):
        betamount = {}
        for number in range(99):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=10).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        smallnumber = min(betamount.values())
        maxvaluenumber = max(betamount, key=betamount.get)
        return maxvaluenumber

    

    def Result(self, obj):
        res = Resultnine.objects.filter(period = obj.id).get()
        return res.result

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

class AdminBetSingle(admin.ModelAdmin):
    list_display = ('period','amount', 'number', 'Userid', 'timing')
    list_per_page = 10
    search_fields = ('period',)
    list_display_links = None

    def all_amount(self, obj):
        betamount = {}
        for number in range(99):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=10).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        smallnumber = min(betamount.values())
        minvaluenumber = min(betamount, key=betamount.get)
        return minvaluenumber

    def Max_number(self, obj):
        betamount = {}
        for number in range(99):
            betdata = BetSingle.objects.filter(period=obj.id, number=number, timing=10).aggregate(Sum('amount'))
            if betdata["amount__sum"] is not None:
                betamount[number] = betdata["amount__sum"]
            if betdata["amount__sum"] is None:
                betamount[number] = 0        
        smallnumber = min(betamount.values())
        maxvaluenumber = max(betamount, key=betamount.get)
        return maxvaluenumber

    

    def Userid(self, obj):
        username = User.objects.filter(id = obj.better).get()
        fullname = Member.objects.filter(username = username.username).get()
        return fullname.username

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False




admin.site.disable_action('delete_selected')
admin.site.register(Member, MemberAdmin)
admin.site.register(Coderequest, RequestcodeAdmin)
admin.site.register(Epin, EpinAdmin)
# admin.site.register(Rewards)
# admin.site.register(Kyc, KycAdmin)
# admin.site.register(Member_profile, MprofileAdmin)
admin.site.register(Earning, EarningAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Widhdraw_requests, WithdrawAdmin)
admin.site.register(newlotteriesthreem, Adminnewlotteriesthreem)
admin.site.register(newlotteries, Adminnewlotteries15m)
admin.site.register(newlotteriesnine, Adminnewlotteriesnine)
admin.site.register(BetSingle, AdminBetSingle)


