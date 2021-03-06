from django.conf.urls import patterns, url

import receivers

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    ModuleCreateView,
    ModuleUpdateView,
    ModuleListView,
    ModuleReadView,

    module_forum_create_wrap,
    ForumList,
    
    module_wiki_create_wrap,
    RequestList,
    HistoryList,
    PublishedList,

    module_activitie_create_wrap,
    ActivitieList,

    module_quiz_create_wrap,
    QuizList,
    QuizMarkingList,

    module_material_create_wrap,
    MaterialList,
    )

from .settings import MODULE_SLUG_PATTERN

"""urls for Module"""
#urls for Updating
routerModuleDetail = ModuleUpdateView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

routerModule = format_suffix_patterns([
    #url(r'^$', api_root),
    
    #create Module
    url(
        r'^new$',
        ModuleCreateView.as_view({'post': 'create'}),
        name='module-create'
    ),

    #retrieve, update, destroy, Module
    url(
    	r'^new/(?P<slug>'+MODULE_SLUG_PATTERN+')$',
    	routerModuleDetail,
    	name='module-update'
    ),

    url(r'^detail/(?P<slug>'+MODULE_SLUG_PATTERN+')$', ModuleReadView.as_view({'get': 'retrieve'}) , name='module_retreive'),


    #get all Modules
    url(
        r'^all$',
        ModuleListView.as_view(),
        name='module-list'
    ),

    
    #FORUM
    #create
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/forum/new$',
        module_forum_create_wrap,
        name='module-forum-create'
    ),

    #list
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/forum/all$',
        ForumList.as_view(),
        name='module-forum-all'
    ),

    #ACTIVITIE
    #create
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/activitie/new$',
        module_activitie_create_wrap,
        name='module-activitie-create'
    ),

    #list
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/activitie/all$',
        ActivitieList.as_view(),
        name='module-activitie-all'
    ),

    #WIKI
    #create
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/wiki/new$',
        module_wiki_create_wrap,
        name='module-wiki-create'
    ),

    #requests
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/wiki/requests$',
        RequestList.as_view(),
        name='module-request-all'
    ),

    #history
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/wiki/history$',
        HistoryList.as_view(),
        name='module-history-all'
    ),

    #Published
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/wiki/published$',
        PublishedList.as_view(),
        name='module-published-all'
    ),

    #EVALUAIONS
    #create
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/quiz/new$',
        module_quiz_create_wrap,
        name='module-quiz-create'
    ),

    #list Quiz
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/quiz/all$',
        QuizList.as_view(),
        name='module-list-quiz-all'
    ),

    #list Marking
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/quiz/marking$',
        QuizMarkingList.as_view(),
        name='module-list-quiz-marking'
    ),

    #MATERIAL
    #create
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/material/new$',
        module_material_create_wrap,
        name='module-material-create'
    ),
    
    #list
    url(
        r'^(?P<module>' + MODULE_SLUG_PATTERN + ')/material/all$',
        MaterialList.as_view(),
        name='module-material-all'
    ),
    

    ])