"""
This file details additional core constraints on DM_AS_11_Core_Framework that
are not expressed in the entries in the SMPTE Metadata Registers.
"""

# Note that there is no "else" statement on any of these. Hence there is no
# restriction on the non-presence of conditional fields when they are not required.
if (AS_11_Closed_Captions_Present):
    CHECK( PRESENT(AS_11_Closed_Captions_Type) )
    CHECK( PRESENT(AS_11_Caption_Language) )
