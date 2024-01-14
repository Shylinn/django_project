from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from .forms import PostUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import Post, Huyen,AuthUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout



def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def welcome_message(request):
    message=''


def my_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'base.html', context)


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        # Lấy người dùng đang đăng nhập
        current_user = self.request.user

        # Lọc bài viết của người dùng đang đăng nhập
        queryset = Post.objects.filter(user=current_user)
        
        return queryset

   

class PostDetailView(DetailView):
    model = Post
    template_name = 'property-single.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.object.user_id
        context['profile'] = AuthUser.objects.get(id=user_id)
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = '__all__'
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        # Thiết lập giá trị của trường user từ người dùng hiện tại
        form.instance.user = self.request.user
        form.instance.user_name = self.request.user.username
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update_form.html'
    fields = '__all__'
    success_url = reverse_lazy('post_list') 

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('post_list')  # Điều hướng đến trang chính sau khi đăng nhập
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')





class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')  
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')  

class HomePostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        queryset = Post.objects.all()


        # Lọc theo quận
        district = self.request.GET.get('district', None)
        if district:
            queryset = queryset.filter(district=district)

        # Lọc theo giá
        price_range = self.request.GET.get('price_range', None)
        if price_range:
            price_range_tuple = tuple(map(int, price_range.split('-')))
            queryset = queryset.filter(price__gte=price_range_tuple[0], price__lte=price_range_tuple[1])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass any additional context variables here
        return context

class UserUpdateView(UpdateView):
    model = AuthUser
    template_name = 'profile_form.html'
    fields = ['username','first_name','last_name','email','phone','profile_image','business']
    success_url = reverse_lazy('post_list')

class PropertiesPostListView(ListView):
    model = Post
    template_name = 'properties.html'
    context_object_name = 'posts'



