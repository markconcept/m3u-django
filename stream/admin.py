from django.contrib import admin

from .models import Channel, EPGChannels, Programmes

def enable_channel(modeladmin, request, queryset):
    ID_EPG = Channel.objects.exclude(epg_id=9999).order_by("-epg_id")[0]
    ID_EPG = ID_EPG.epg_id+1
    queryset.update(channel_enabled=True, epg_id=ID_EPG)
enable_channel.short_description = "Enable Channel"

def disable_channel(modeladmin, request, queryset):
    queryset.update(channel_enabled=False, epg_id=9999)
disable_channel.short_description = "Disable Channel"


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('epg_id', 'channel_name', 'channel_enabled')
    ordering = ('epg_id',)
    actions = [enable_channel, disable_channel]


admin.site.register(Channel, ChannelAdmin)
admin.site.register(EPGChannels)
admin.site.register(Programmes)
