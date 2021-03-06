from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

import receivers

from .views import (
#    BadgeCreate,
#    BadgeDetail,
    BadgeList,
#    BadgesUpdateView,
#    AwardUpdateView,
#    AwardDetail,
    AwardList,
    AwardListAll,
    ProgressDetail,
    ScoresView,
    ScoresViewAll,

    VoteCreateView,
    VoteListView, )



"""
routerBadgesDetail = BadgesUpdateView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})
"""

routerBadges = format_suffix_patterns([
    #url(r'^$', api_root),
    
    #create
    #url(r'^badge$', BadgeCreate.as_view({'post': 'create'}), name='badge-create'),

    #retrieve, update, destroy
    #url(r'^badge/(?P<pk>[0-9]+)$', routerBadgesDetail, name='badge-update'),

    #detail
    #url(r'^badge/detail/(?P<pk>[0-9]+)$', BadgeDetail.as_view({'get': 'retrieve'}), name='badge-detail'),

    #get all asks 
    url(r'^badge/all$', BadgeList.as_view() , name='badge-list'),

    #----------------------------------------------------------------------
    #progress badge
    #url(r'^badge/progress$', ProgressCreate.as_view({'post': 'create'}) , name='Progress-badge-create'),

    # trae los progresos del usuario en las medallas
    url(r'^badge/progress/detail/(?P<pk>[0-9]+)$', ProgressDetail.as_view() , name='Progress-badge-detail'),

    ])

"""
routerAwardDetail = AwardUpdateView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})
"""

routerAward = format_suffix_patterns([
    #url(r'^$', api_root),
    
    #create
    #url(r'^award$', AwardCreate.as_view({'post': 'create'}), name='badge-create'),

    #retrieve, update, destroy
    #url(r'^award/(?P<pk>[0-9]+)$', routerAwardDetail, name='badge-update'),

    #detail
    #url(r'^award/detail/(?P<pk>[0-9]+)$', AwardDetail.as_view({'get': 'retrieve'}), name='badge-detail'),

    # all awadr of all users
    url(r'^award/all/$', AwardListAll.as_view() , name='badge-list-All'),

    # for profile all awards
    url(r'^award/all/(?P<pk>[0-9]+)$', AwardList.as_view() , name='badge-list'),

    ])



routerScores = format_suffix_patterns([
    #url(r'^scores/
    #create
    url(r'^scores/$', ScoresView.as_view({'post': 'create'}), name='scores-create'),
    url(r'^scores/(?P<pk>[0-9]+)$', ScoresView.as_view({'get': 'retrieve', 'put':'update'}), name='scores'),
    url(r'^scores/all$', ScoresViewAll.as_view(), name='scoresAll'),

    ])


#### Votes

routerVotes = format_suffix_patterns([
    #url(r'^$', api_root),
    
    #create
    url(r'^vote$', VoteCreateView.as_view({'post': 'create'}), name='vote-give'),

    url(r'^vote/detail/(?P<pk>[0-9]+)$', VoteListView.as_view() , name='vote-detail'),

    ])
