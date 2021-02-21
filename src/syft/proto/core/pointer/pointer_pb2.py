# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/pointer/pointer.proto

# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/pointer/pointer.proto",
    package="syft.core.pointer",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n proto/core/pointer/pointer.proto\x12\x11syft.core.pointer\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"\xd3\x01\n\x07Pointer\x12"\n\x1apoints_to_object_with_path\x18\x01 \x01(\t\x12\x14\n\x0cpointer_name\x18\x02 \x01(\t\x12-\n\x0eid_at_location\x18\x03 \x01(\x0b\x32\x15.syft.core.common.UID\x12\'\n\x08location\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0c\n\x04tags\x18\x05 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x13\n\x0bobject_type\x18\x07 \x01(\tb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_POINTER = _descriptor.Descriptor(
    name="Pointer",
    full_name="syft.core.pointer.Pointer",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="points_to_object_with_path",
            full_name="syft.core.pointer.Pointer.points_to_object_with_path",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="pointer_name",
            full_name="syft.core.pointer.Pointer.pointer_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id_at_location",
            full_name="syft.core.pointer.Pointer.id_at_location",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="location",
            full_name="syft.core.pointer.Pointer.location",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tags",
            full_name="syft.core.pointer.Pointer.tags",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="syft.core.pointer.Pointer.description",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="object_type",
            full_name="syft.core.pointer.Pointer.object_type",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=124,
    serialized_end=335,
)

_POINTER.fields_by_name[
    "id_at_location"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_POINTER.fields_by_name[
    "location"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name["Pointer"] = _POINTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pointer = _reflection.GeneratedProtocolMessageType(
    "Pointer",
    (_message.Message,),
    {
        "DESCRIPTOR": _POINTER,
        "__module__": "proto.core.pointer.pointer_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.pointer.Pointer)
    },
)
_sym_db.RegisterMessage(Pointer)


# @@protoc_insertion_point(module_scope)
