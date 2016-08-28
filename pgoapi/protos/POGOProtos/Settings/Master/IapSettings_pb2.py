# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/Master/IapSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Settings/Master/IapSettings.proto',
  package='POGOProtos.Settings.Master',
  syntax='proto3',
  serialized_pb=_b('\n,POGOProtos/Settings/Master/IapSettings.proto\x12\x1aPOGOProtos.Settings.Master\"\x8c\x02\n\x0bIapSettings\x12\x19\n\x11\x64\x61ily_bonus_coins\x18\x01 \x01(\x05\x12(\n daily_defender_bonus_per_pokemon\x18\x02 \x03(\x05\x12*\n\"daily_defender_bonus_max_defenders\x18\x03 \x01(\x05\x12%\n\x1d\x64\x61ily_defender_bonus_currency\x18\x04 \x03(\t\x12\"\n\x1amin_time_between_claims_ms\x18\x05 \x01(\x03\x12\x1b\n\x13\x64\x61ily_bonus_enabled\x18\x06 \x01(\x08\x12$\n\x1c\x64\x61ily_defender_bonus_enabled\x18\x07 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IAPSETTINGS = _descriptor.Descriptor(
  name='IapSettings',
  full_name='POGOProtos.Settings.Master.IapSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='daily_bonus_coins', full_name='POGOProtos.Settings.Master.IapSettings.daily_bonus_coins', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_defender_bonus_per_pokemon', full_name='POGOProtos.Settings.Master.IapSettings.daily_defender_bonus_per_pokemon', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_defender_bonus_max_defenders', full_name='POGOProtos.Settings.Master.IapSettings.daily_defender_bonus_max_defenders', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_defender_bonus_currency', full_name='POGOProtos.Settings.Master.IapSettings.daily_defender_bonus_currency', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_time_between_claims_ms', full_name='POGOProtos.Settings.Master.IapSettings.min_time_between_claims_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_bonus_enabled', full_name='POGOProtos.Settings.Master.IapSettings.daily_bonus_enabled', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_defender_bonus_enabled', full_name='POGOProtos.Settings.Master.IapSettings.daily_defender_bonus_enabled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=345,
)

DESCRIPTOR.message_types_by_name['IapSettings'] = _IAPSETTINGS

IapSettings = _reflection.GeneratedProtocolMessageType('IapSettings', (_message.Message,), dict(
  DESCRIPTOR = _IAPSETTINGS,
  __module__ = 'POGOProtos.Settings.Master.IapSettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.IapSettings)
  ))
_sym_db.RegisterMessage(IapSettings)


# @@protoc_insertion_point(module_scope)