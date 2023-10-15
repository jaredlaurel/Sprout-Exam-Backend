from urllib.parse import urlencode


class BaseUtils:
    def paginate(
        self,
        api_url: str,
        page: int,
        per_page: int,
        order_by: str,
        total: int,
        **kwargs,
    ) -> dict:
        """Paginate

        Args:
            api_url (str): API Base Url
            page (int): Page
            per_page (int): Per Page or Limit
            order_by (str): Order By (eg. created|<asc|desc>)
            total (int): Total Items

        Returns:
            dict: Pagination Object
        """

        to_item = page * per_page
        if to_item > total:
            to_item = total

        last_page = int(total / per_page)

        if int(total % per_page) >= 1:
            last_page += 1

        # Previous Page
        prev_page_url = None
        if page > 1:
            prev_page_url = self._generate_page_url(
                api_url=api_url,
                order_by=order_by,
                page=page - 1,
                per_page=per_page,
                **kwargs,
            )

        # Next Page
        next_page_url = None
        if page < last_page:
            next_page_url = self._generate_page_url(
                api_url=api_url,
                order_by=order_by,
                page=page + 1,
                per_page=per_page,
                **kwargs,
            )

        # First Page
        first_page_url = self._generate_page_url(
            api_url=api_url, order_by=order_by, page=1, per_page=per_page, **kwargs
        )

        # Last Page
        last_page_url = self._generate_page_url(
            api_url=api_url,
            order_by=order_by,
            page=last_page,
            per_page=per_page,
            **kwargs,
        )

        pagination = {
            "total": total,
            "per_page": per_page,
            "current_page": page,
            "last_page": last_page,
            "first_page_url": first_page_url,
            "last_page_url": last_page_url,
            "next_page_url": next_page_url,
            "prev_page_url": prev_page_url,
            "path": api_url,
            "from": page,
            "to": to_item,
        }

        return pagination

    def _generate_page_url(
        self, api_url: str, order_by: str, page: int, per_page: int, **kwargs
    ) -> str:
        """Generate Page Url

        Args:
            api_url (str): API Base Url
            order_by (str): Order By (eg. created|<asc|desc>)
            page (int): Page
            per_page (int): Per Page or Limit

        Returns:
            str: Generated Page Url
        """
        query = [("order_by", order_by), ("page", page), ("per_page", per_page)]
        query.extend(list(kwargs.items()))
        query_string = urlencode(query)
        page_url = "{0}?{1}".format(api_url, query_string)

        return page_url
