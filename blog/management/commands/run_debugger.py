from django.core.management.base import BaseCommand

from blog.queries import (post_list, post_list_bad, post_list_select_related_good, post_list_select_prefetch_related,
                        post_list_select_related_2, post_list_bad_2, post_list_prefetch_related_good,
                        user_list_bad, user_list_select_related_good, post_list_prefetch_related_good_2, post_list_prefetch_related_bad,
                        post_list_prefetch_related_good_3,
                        )


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # post_list()
        # post_list_bad()
        # post_list_select_related_good()
        # user_list_bad()
        # user_list_select_related_good()
        # post_list_select_related_2()
        # post_list_bad_2()
        # post_list_prefetch_related_good()
        # post_list_prefetch_related_good_2()
        # post_list_prefetch_related_bad()
        # post_list_prefetch_related_good_3()
        post_list_select_prefetch_related()