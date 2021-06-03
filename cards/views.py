from cards.forms import FlashCardsForm
from cards.models import FlashCards
from django.shortcuts import redirect, render
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic import ListView,DetailView
from .models import FlashCards
# from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Create your views here.

# # class FlashCardsListView(ListView):
#     model = FlashCards
#     template_name = 'cards/flash_cards_list.html'
#     ordering = ['-timestamp']
#     paginate_by = 9

#     def get_context_data(self, **kwargs):
#         context = super(FlashCardsListView, self).get_context_data(**kwargs)
#         return context

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             return FlashCards.objects.filter(title__icontains=query)
#         else:
#             return FlashCards.objects.all()
            
# class FlashCardsCreateView(SuccessMessageMixin, CreateView):
#     model = FlashCards
#     template_name = 'cards/flash_cards_form.html'
#     fields = ['title', 'description','subject']
#     success_message = "The Flash Card %(title) was created successfully!"
  
#     def form_valid(self, form):
#         form.instance.creator = self.request.user
#         return super().form_valid(form)            
        
        
        
# class FlashCardsDetailView(DetailView):
#     model = FlashCards       
        
    
def home(request):
    cards = FlashCards.objects.all()
    ctx = {'cards':cards}
    
    return render (request, 'cards/flash_cards_list.html', ctx )

        
def flashCardsCreateView(request):
    form = FlashCardsForm()
    
    if request.method == 'POST':
        form = FlashCardsForm(request.POST)
        if form.is_valid():
            form.save()
        
            messages.success(request, 'Successfully Added.')
            return redirect('cards-home')
    
    ctx = {'form':form}
    
    return render(request,'cards/flash_cards_form.html', ctx)
    
# def  flashCardsListView(request):
    