"""
This file details additional core constraints on DM_AS_11_UKDPP_Framework that
are not expressed in the entries in the SMPTE Metadata Registers.
"""

# Note that there is no "else" statement on any of these. Hence there is no
# restriction on the non-presence of conditional fields when they are not required.
if PRESENT(UKDPP_Other_Identifier):
    CHECK( PRESENT(UKDPP_Other_Identifier_Type) )

if UKDPP_3D:
    CHECK( PRESENT(UKDPP_3D_Type) )

if UKDPP_PSE_Pass != PSE_Not_tested:
    CHECK( PRESENT(UKDPP_PSE_Manufacturer) )
    CHECK( PRESENT(UKDPP_PSE_Version) )

if UKDPP_Audio_Description_Present:
    CHECK( PRESENT(UKDPP_Audio_Description_Type) )

if UKDPP_Open_Captions_Present:
    CHECK( PRESENT(UKDPP_Open_Captions_Type) )
    CHECK( PRESENT(UKDPP_Open_Captions_Language) )

if UKDPP_Signing_Present in [Signing_Yes, Signing_Signer_only]:
    CHECK( PRESENT(UKDPP_Sign_Language) )

if PRESENT(UKDPP_Programme_Has_Text) and UKDPP_Programme_Has_Text:
    CHECK( PRESENT(UKDPP_Programme_Text_Language) )
