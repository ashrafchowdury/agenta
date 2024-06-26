# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from ...types.image import Image
from ...types.uri import Uri
from .types.container_templates_response import ContainerTemplatesResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ContainersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def build_image(self, *, app_id: str, base_name: str, tar_file: typing.IO) -> Image:
        """
        Builds a Docker image from a tar file containing the application code.

        Args:
        app_id (str): The ID of the application to build the image for.
        base_name (str): The base name of the image to build.
        tar_file (UploadFile): The tar file containing the application code.
        stoken_session (SessionContainer): The session container for the user making the request.

        Returns:
        Image: The Docker image that was built.

        Parameters:
            - app_id: str.

            - base_name: str.

            - tar_file: typing.IO.
        ---
        from agenta.client import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.containers.build_image(
            app_id="app_id",
            base_name="base_name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "containers/build_image"
            ),
            params=remove_none_from_dict({"app_id": app_id, "base_name": base_name}),
            data=jsonable_encoder({}),
            files={"tar_file": tar_file},
            headers=self._client_wrapper.get_headers(),
            timeout=600,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Image, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def restart_container(self, *, variant_id: str) -> typing.Dict[str, typing.Any]:
        """
        Restart docker container.

        Args:
        payload (RestartAppContainer) -- the required data (app_name and variant_name)

        Parameters:
            - variant_id: str.
        ---
        from agenta.client import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.containers.restart_container(
            variant_id="variant_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                "containers/restart_container",
            ),
            json=jsonable_encoder({"variant_id": variant_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.Any], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def container_templates(self) -> ContainerTemplatesResponse:
        """
        Returns a list of templates available for creating new containers.

        Parameters:
        stoken_session (SessionContainer): The session container for the user.

        Returns:

        Union[List[Template], str]: A list of templates or an error message.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "containers/templates"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ContainerTemplatesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def construct_app_container_url(
        self,
        *,
        base_id: typing.Optional[str] = None,
        variant_id: typing.Optional[str] = None,
    ) -> Uri:
        """
        Constructs the URL for an app container based on the provided base_id or variant_id.

        Args:
        base_id (Optional[str]): The ID of the base to use for the app container.
        variant_id (Optional[str]): The ID of the variant to use for the app container.
        request (Request): The request object.

        Returns:
        URI: The URI for the app container.

        Raises:
        HTTPException: If the base or variant cannot be found or the user does not have access.

        Parameters:
            - base_id: typing.Optional[str].

            - variant_id: typing.Optional[str].
        ---
        from agenta.client import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.containers.construct_app_container_url()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "containers/container_url"
            ),
            params=remove_none_from_dict(
                {"base_id": base_id, "variant_id": variant_id}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Uri, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncContainersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def build_image(
        self, *, app_id: str, base_name: str, tar_file: typing.IO
    ) -> Image:
        """
        Builds a Docker image from a tar file containing the application code.

        Args:
        app_id (str): The ID of the application to build the image for.
        base_name (str): The base name of the image to build.
        tar_file (UploadFile): The tar file containing the application code.
        stoken_session (SessionContainer): The session container for the user making the request.

        Returns:
        Image: The Docker image that was built.

        Parameters:
            - app_id: str.

            - base_name: str.

            - tar_file: typing.IO.
        ---
        from agenta.client import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.containers.build_image(
            app_id="app_id",
            base_name="base_name",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "containers/build_image"
            ),
            params=remove_none_from_dict({"app_id": app_id, "base_name": base_name}),
            data=jsonable_encoder({}),
            files={"tar_file": tar_file},
            headers=self._client_wrapper.get_headers(),
            timeout=600,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Image, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def restart_container(
        self, *, variant_id: str
    ) -> typing.Dict[str, typing.Any]:
        """
        Restart docker container.

        Args:
        payload (RestartAppContainer) -- the required data (app_name and variant_name)

        Parameters:
            - variant_id: str.
        ---
        from agenta.client import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.containers.restart_container(
            variant_id="variant_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                "containers/restart_container",
            ),
            json=jsonable_encoder({"variant_id": variant_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.Any], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def container_templates(self) -> ContainerTemplatesResponse:
        """
        Returns a list of templates available for creating new containers.

        Parameters:
        stoken_session (SessionContainer): The session container for the user.

        Returns:

        Union[List[Template], str]: A list of templates or an error message.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "containers/templates"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ContainerTemplatesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def construct_app_container_url(
        self,
        *,
        base_id: typing.Optional[str] = None,
        variant_id: typing.Optional[str] = None,
    ) -> Uri:
        """
        Constructs the URL for an app container based on the provided base_id or variant_id.

        Args:
        base_id (Optional[str]): The ID of the base to use for the app container.
        variant_id (Optional[str]): The ID of the variant to use for the app container.
        request (Request): The request object.

        Returns:
        URI: The URI for the app container.

        Raises:
        HTTPException: If the base or variant cannot be found or the user does not have access.

        Parameters:
            - base_id: typing.Optional[str].

            - variant_id: typing.Optional[str].
        ---
        from agenta.client import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.containers.construct_app_container_url()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "containers/container_url"
            ),
            params=remove_none_from_dict(
                {"base_id": base_id, "variant_id": variant_id}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Uri, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
