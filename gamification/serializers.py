from rest_framework import serializers

from badger import views
from badger.models import *
from badger.signals import *

from .models import Scores, Votes
from module.models import Module
from quiz.models import Quiz
from activitie.models import ActivitieParent

class BadgeCreateSerializer(serializers.ModelSerializer):
    """
    Serializer Class Badge
    """

    class Meta():
        model = Badge


from users.models import User
class AwardCreateSerializer(serializers.ModelSerializer):
    """
    Serializer Class Award
    """
    badge = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_badge(self, obj):
        module = Module.objects.get(slug = obj.badge.slug)
        return {'title': obj.badge.title, 'img': module.photo.url}


    def get_user(self, obj):
        return {obj.user.first_name+' '+obj.user.last_name}
        
        

    class Meta():
        model = Award


class ProgressCreateSerializer(serializers.ModelSerializer):
    """
    Serializer Class Progress
    """
    badge = serializers.SerializerMethodField()

    def get_badge(self, obj):

        module = Module.objects.get(slug= obj.badge.slug)
        return {'slug':obj.badge.slug, 'title': obj.badge.title}

    class Meta():
        model = Progress
        fields = ('percent', 'badge',)



#----------------

from django.core.exceptions import PermissionDenied
from  gamification.signals import update_points_end_badge

class ScoresUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer Class Nomination
    """
    id_event = serializers.SerializerMethodField()

    def get_id_event(self, obj):
        if obj.event == 'Activity':
            print 'entro Activity'

            activitie = ActivitieParent.objects.get(id = obj.id_event)
            print activitie
            return {'name':activitie.name,'id':activitie.id}
        else:
            print 'entro Quiz'
            quiz = Quiz.objects.get(id = obj.id_event)
            print quiz
            return {'name':quiz.title, 'id': quiz.id}
        
        return{}

    def update(self, instance, validated_data, **kwargs):
        try:
            # se emite senal para actualizar los puntos del progreso
            update_points_end_badge.send(sender = ScoresUpdateSerializer, old_score = instance.score, new_score = validated_data.get('score'), id_instance = instance.id_event, type_instance = instance.event)

            instance.event = validated_data.get('event', instance.event)
            instance.id_event = validated_data.get('id_event', instance.id_event)
            instance.score = validated_data.get('score', instance.score)
            
            instance.save()
            return instance
        except IntegrityError:
            raise PermissionDenied

        
    class Meta():
        model = Scores


# -------
# Votes
#

from django.db import IntegrityError
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist


class VotesSerializer(serializers.ModelSerializer):
    """
    Serializer Class to Votes
    """
    previous = serializers.SerializerMethodField()

    def get_previous(self, obj_thread):
        return self.previous

    def create(self, validated_data):
        try:
            user = self.context['request'].user
            thread = validated_data['thread']
            vote = validated_data['vote']
            try:
                self.previous = int(Votes.objects.get(thread=thread, author=user).vote)
            except ObjectDoesNotExist, e:
                self.previous = ""

            voted = Votes.create(author=user, thread=thread, vote=vote)
            return voted

        except IntegrityError, e:
            raise PermissionDenied

    class Meta():
        model = Votes
        fields = ('thread', 'vote', 'previous',  )
        read_only_fields = ('previous', )


class ListVotesSerializer(serializers.ModelSerializer):
    thread = serializers.SerializerMethodField()
    up_votes = serializers.SerializerMethodField()
    down_votes = serializers.SerializerMethodField()
    
    def get_thread(self, obj_thread):
        return obj_thread.pk
    
    def get_up_votes(self, obj_thread):
        # 0 is up vote
        return Votes.objects.filter(thread=obj_thread.pk, vote=0).count()

    def get_down_votes(self, obj_thread):
        # 1 is down vote
        return Votes.objects.filter(thread=obj_thread.pk, vote=1).count()

    class Meta():
        model = Votes
        fields = ('thread', 'up_votes', 'down_votes', )

