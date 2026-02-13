from django.contrib import admin
from .models import Assignment, UserAssignment, Comment, Goal, GoalTask

# --- Comment inline prie UserAssignment ---
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('created',)


# --- UserAssignment admin ---
@admin.register(UserAssignment)
class UserAssignmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'assignment', 'is_shared', 'created')
    list_filter = ('is_shared', 'created')
    search_fields = ('user__username', 'assignment__title')
    inlines = [CommentInline]


# --- Assignment admin ---
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)


# --- GoalTask inline prie Goal ---
class GoalTaskInline(admin.TabularInline):
    model = GoalTask
    extra = 1


# --- Goal admin ---
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')
    search_fields = ('title', 'user__username')
    inlines = [GoalTaskInline]