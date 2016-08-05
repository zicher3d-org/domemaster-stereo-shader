///////////////////////////////////////////////////////////////////////////////
// Copyright 1986, 2016 NVIDIA Corporation. All rights reserved.
///////////////////////////////////////////////////////////////////////////////
// Created:	09.01.06
// Module:	api
// Purpose:	mental ray C++ shader interface extensions
///////////////////////////////////////////////////////////////////////////////

/// \file mi_shader_if.h
/// mental ray C++ shader interface extensions.
///
/// This is a new C++ interface for shaders which extends the existing C-style
/// shader interface to mental ray. It is implemented as abstract interface
/// classes which do not require symbol lookups across dynamically loadable
/// library boundaries, like shaders. It also makes it possible to provide new,
/// even incompatible versions of the interface later.
///
/// Binaries which have been compiled with an older version of this header file
/// typically work with newer versions of this interface as long as the new
/// member functions have been appended at the end of the existing classes.
///
/// mi_shader_if.h is included from shader.h if the shader is compiled as C++
/// code; a shader does not need to include mi_shader_if.h directly.
/// 
/// The namespace alias shader_v3 is used to avoid conflict of inlined 
/// symbols between shader libraries compiled with different version.
/// On Linux platforms, this relaxes the requirement to link shader libraries
/// with the -Bsymbolic option.

#ifndef MI_SHADER_IF_H
#define MI_SHADER_IF_H

// if file is included internally
#if !defined(SHADER_H)
#include <mi_raylib.h>
#include <mi_lib.h>
#include <mi_shader.h>
#endif

#ifndef __cplusplus
#error mi_shader_if.h requires C++ compilation
#endif


/// \brief version number of the interface
static const int mi_ray_interface_version = 3;

namespace mi {
namespace shader_v3 {
struct Interface;
}}


/// \brief Acquire an instance of the mental ray C++ shader interface extensions.
///
/// \param version is the version number of the requested interface class
/// and should usually be left at the default value.
/// The passed version argument is used to support multiple different interface 
/// versions and should usually be the value of the variable
/// mi_ray_interface_version in the defining header file. A future version of
/// mental ray may optionally return a pointer to a newer version of the 
/// interface of a different type or in a different namespace, identified by a
/// different version number.
///
/// \return The returned pointer points to an object in mental ray which
/// contains the interface functions as virtual methods (hence it is possible to
/// call the interface routines from a dynamically loaded library without
/// resolving the routine in a symbol table). The caller may not attempt to
/// modify or delete the returned object but should call the
/// mi::shader::Interface::release() method when done.

extern "C" mi::shader_v3::Interface *mi_get_shader_interface(
    int version = mi_ray_interface_version);

//! \brief Top level namespace of mental ray
namespace mi {


/// \brief Namespace containing mental ray C++ shader interface extensions
///
/// The mental ray C++ interface is completely contained in the shader namespace.
/// \note This name may change later in order to support multiple versions of
/// the interface.
namespace shader_v3 {


/// forward declarations
class Options;
class LightList;
class MISLightList;
class Framebuffer;
class Map_status;
class Map_base;
class Edit_map_dbhandle;
class Access_map_dbhandle;
class Access_map;
class Edit_map;
class Map_declaration_base;
class Map_iterator_base;
class Map_element_base;
class Map_lookup_base;
class Bsdf;
class Access_bsdf;
class Subdivision34;
class Mip_remap;



/// \brief Top level C++ mental ray interface extensions.
///
/// This class is the top level access to the C++ shader interface extensions.
/// All other C++ extensions like mi::shader::Options and
/// mi::shader::LightIterator are accessible through this class.
///
/// An instance of the Interface must be acquired by calling
/// mi_get_shader_interface() or the static method Interface::get().
/// When the interface is no more needed, it must be released by calling
/// Interface::release():
/// \code
/// mi::shader::Interface *iface = mi::shader::Interface::get();
/// // do something with it...
/// iface->release();
/// \endcode
/// 
/// The C++ interface extensions are implemented as virtual functions in this
/// interface struct in order to avoid linking and symbol lookup problems.
/// The interface is defined in the header file mi_shader_if.h.

struct Interface {
  public:
    /// \brief Acquire an instance of the interface.
    ///
    /// This static method is equivalent to the function
    /// mi_get_shader_interface(), see there fore more information.
    /// This static function can be used as follows:
    /// \code
    /// mi::shader::Interface *iface = mi::shader::Interface::get();
    /// \endcode
    /// \param version is the version number of the requested interface class,
    /// usually no version argument needs to be passed.
    /// \return The returned pointer points to an object in mental ray which
    /// contains the interface functions as virtual methods (hence it is 
    /// possible to call the interface routines from a dynamically loaded 
    /// library without resolving the routine in a symbol table). The caller may
    /// not attempt to modify or delete the returned object but should call the
    /// mi::shader::Interface::release() method when done.
    static inline Interface* get(
	int 		version = mi_ray_interface_version)
    { 
	return mi_get_shader_interface(version); 
    }

    /// \brief Access to string options.
    ///
    /// This may later be extended to also access all other options from the
    /// miOptions structure. This function can be used as follows:
    /// \code
    /// Options *stringOptions = interface->getOptions(options->string_options);
    /// \endcode
    /// \param string_options is the tag of the string options, taken from
    /// the string_options field of the miOptions structure to be read or
    /// modified.
    /// It must be valid throughout the use of the Options instance.
    /// \return A pointer to an interface class. The Options::release() method
    /// should be called when done.
    virtual Options *getOptions(
	miTag 		string_options);

    /// \brief Framebuffer factory function.
    ///
    /// \return a database tag for an empty framebuffer collection.
    virtual miTag createFramebuffer();

    /// \brief Creates a copy of the framebuffer collection.
    ///
    /// \param old_buffer_tag A database tag for the framebuffer to copy	
    /// \return a database tag for a copy of framebuffer collection.
    virtual miTag copyFramebuffer(
        miTag           old_buffer_tag);

    /// \deprecated
    /// \brief Internal function to create a light list.
    ///
    /// This may be used to generate light iterators. This method is needed
    /// by the LightIterator::LightIterator() constructor. Usually there is no need to invoke
    /// this method directly.
    /// \param state provided the method with the current rendering state. From
    /// the state the current instance light list may be deduced.
    /// \param slist is an optional list of light tags. If provided, this list
    /// will be used instead of the default instance light list.
    /// \param n gives the number of light tags in the optional light list.
    /// \return the method returns a pointer to a LightList.
    virtual LightList *createLightList(
	miState		*state, 
	miTag 		*slist = 0, 
	int 		n = 0);

    /// \brief Release (delete) the instance of the interface.
    ///
    /// An interface acquired with mi_get_shader_interface() or 
    /// mi::shader::Interface::get() must be released with this call when 
    /// done. The call may delete the object, and the interface may no longer be
    /// used afterwards.
    virtual void release();


    /// \brief Used internally by LightIterator to create a light list.
    ///
    /// This may be used to generate light iterators. This method is needed
    /// by the LightIterator::LightIterator() constructor. Usually there is no need to invoke
    /// this method directly.
    /// \param state provided the method with the current rendering state. From
    /// the state the current instance light list may be deduced.
    /// \param axis specifies the axis for the light cone. The value should be normalized.
    /// \param spread_cos specifies the cosine of the angle to the light cone axis.
    /// \param slist is an optional list of light tags. If provided, this list
    /// will be used instead of the default instance light list.
    /// \param n gives the number of light tags in the optional light list.
    /// \return the method returns a pointer to a LightList.
    virtual LightList *createLightList(
	miState		*state,
	const miVector	&axis,
	miScalar	spread_cos,
	miTag		*slist = 0, 
	int 		n = 0);


    /// \brief Creation of map. 
    ///
    /// This function is wrapped by the Edit_map class and should not be
    /// used directly.
    /// \param map_declaration is the declaration (possibly NULL) of the new map 
    /// \return pointer to the newly created map
    virtual Edit_map_dbhandle *createMap(
	const Map_declaration_base  *map_declaration = 0);

    /// \brief Read-only access to a map in the DB.
    ///
    /// This function is wrapped by the Access_map class and should not be
    /// used directly
    /// \param map_tag database tag of the map
    /// \return pointer to the map
    virtual Access_map_dbhandle *accessMap(
	const miTag 		map_tag);

    /// \brief Read-write access to a map in the DB.
    ///
    /// This function is wrapped by the Edit_map class and should not be
    /// used directly
    /// \param map_tag database tag of the map
    /// \return pointer to the map
    virtual Edit_map_dbhandle *editMap(
	const miTag 		map_tag);

    /// \brief Read-only access to a map to be read from file.
    ///
    /// This function is wrapped by the Access_map class and should not be
    /// used directly
    /// \param filename the file name of the map to read
    /// \param status a status code
    /// \return pointer to the map
    virtual Access_map_dbhandle *accessMap(
	const char		*filename,
	Map_status		*status);

    /// \brief Read-write access to a map to be read from file.
    ///
    /// This function is wrapped by the Edit_map class and should not be
    /// used directly
    /// \param filename the file name of the map to read
    /// \param status a status code
    /// \return pointer to the map
    virtual Edit_map_dbhandle *editMap(
	const char		*filename,
	Map_status		*status);

    /// \brief Creation of a map declaration.
    ///
    /// This function is wrapped by the Map_declaration class and
    /// should not be used directly
    /// \param dimension is the dimension of the position
    /// \return pointer to the newly created map declaration
    virtual Map_declaration_base *createMapDeclaration(
	const miUint		dimension);

    /// \brief Copy of a map declaration.
    ///
    /// This function is wrapped by the Map_declaration class and
    /// should not be used directly
    /// \param other is the handle of the declaration to copy
    /// \param status is a status code
    /// \return pointer to the newly copied map declaration
    virtual Map_declaration_base *copyMapDeclaration(
	const Map_declaration_base  *other,
	Map_status		    *status);

    /// \brief Copy of the declaration of a map element.
    ///
    /// This function is wrapped by the Map_declaration class and
    /// should not be used directly
    /// \param map_element is the map element to get a copy of the decl from
    /// \param status is a status code
    /// \return pointer to the newly copied map declaration
    virtual Map_declaration_base *copyMapDeclaration(
	const Map_element_base	*map_element,
	Map_status		*status);

    /// \brief Copy of the declaration of a map.
    ///
    /// This function is wrapped by the Map_declaration class and
    /// should not be used directly
    /// \param map is the map to get a copy of the declaration from
    /// \param status is a status code
    /// \return pointer to the newly copied map declaration
    virtual Map_declaration_base *copyMapDeclaration(
	const Map_base		*map,
	Map_status		*status);

    /// \brief Creation of a map element.
    ///
    /// This function is wrapped by the Map_element class and
    /// should not be used directly
    /// \param declaration is the (possible) declaration to use
    /// \return pointer to the newly created map element
    virtual Map_element_base *createMapElement(
	const Map_declaration_base  *declaration = 0);

    /// \brief Copy of a map element.
    ///
    /// This function is wrapped by the Map_element class and
    /// should not be used directly
    /// \param other is the element to copy
    /// \return pointer to the newly copied map element
    virtual Map_element_base *copyMapElement(
	const Map_element_base	*other);

    /// \brief Creation of a map iterator.
    ///
    /// This function is wrapped by the Access_map_iterator/edit classes
    /// and should not be used directly
    /// \param map is the map to attach the iterator to
    /// \param status is a status code
    /// \return pointer to the newly created map iterator
    virtual Map_iterator_base *createMapIterator(
	const Map_base		*map,
	Map_status		*status);

    /// \brief Copy of a map iterator.
    ///
    /// This function is wrapped by the map_iterator_access/edit classes
    /// and should not be used directly
    /// \param other is the iterator to copy
    /// \param status is a status code
    /// \return pointer to the newly copied map iterator
    virtual Map_iterator_base *copyMapIterator(
	const Map_iterator_base	*other,
	Map_status		*status);

    /// \brief Creation of a map lookup.
    ///
    /// This function is wrapped by the Map_lookup class
    /// and should not be used directly
    /// \param map is the map to attach the lookup to
    /// \param status is a status code
    /// \return pointer to the newly created map lookup
    virtual Map_lookup_base *createMapLookup(
	const Map_base		*map,
	Map_status		*status);

    /// \brief Copy of a map lookup.
    ///
    /// This function is wrapped by the Map_lookup class
    /// and should not be used directly
    /// \param other is the lookup to copy
    /// \param status is a status code
    /// \return pointer to the newly created map lookup
    virtual Map_lookup_base *copyMapLookup(
	const Map_lookup_base	*other,
	Map_status		*status);

/// \cond internal (for linkage, declare virtual methods which cannot be private)

    /// \brief Read-only access to framebuffer. 
    ///
    /// This functions is wrapped by the Access_fb class and should
    /// not be used directly
    /// \param buffer_tag database tag for the framebuffer collection
    /// \return pointer to the framebuffer class
    virtual const Framebuffer *accessFramebuffer(
	miTag 		buffer_tag);

    /// \brief Release read-only access to framebuffer. 
    ///
    /// This functions is wrapped by the Access_fb class and should
    /// not be used directly
    /// \param buffer_tag database tag for the framebuffer collection
    /// \param pointer to the framebuffer class
    /// \return returns true on success
    virtual bool releaseFramebuffer(
	const Framebuffer	*buffer,			   
	miTag 			buffer_tag);

    /// \brief Read-write access to framebuffer. 
    ///
    /// This functions is wrapped by the Edit_fb class and should
    /// not be used directly
    /// \param buffer_tag database tag for the framebuffer collection
    /// \return pointer to the framebuffer class
    virtual Framebuffer *editFramebuffer(
	miTag 		buffer_tag);

    /// \brief Release read-write access to framebuffer. 
    ///
    /// This functions is wrapped by the Access_fb class and should
    /// not be used directly
    /// \param buffer_tag database tag for the framebuffer collection
    /// \param pointer to the framebuffer class
    /// \return returns true on success
    virtual bool releaseFramebuffer(
	Framebuffer		*buffer,			   
	miTag 			buffer_tag);

/// \endcond

/// \cond internal

    /// \brief Allocate a \c Bsdf instance.
    ///
    /// This function calls the \c bsdf shader attached to \c state->material
    /// and requests a new \c Bsdf instance.
    /// See \c Access_bsdf for details.
    virtual Bsdf* allocBsdf(
	    miState* 		state);
 
    /// \brief Release a \c Bsdf instance.
    ///
    /// This function calls the \c bsdf shader attached to \c state->material
    /// and requests the destruction of \p bsdf.
    /// See \c Access_bsdf for details.
    virtual void releaseBsdf(
	    Bsdf* 		bsdf, 
	    miState* 		state);

/// \endcond

    /// \brief Provide access to (allocate) the Subdivision34 class.
    /// \param tag is the MI::SDS::Subdiv34 class tag
    virtual Subdivision34 * accessSubdivision34(
	    miTag		tag);

    /// \brief Release (delete) the Subdivision34 class.
    /// \param subdiv34 is the pointer returned by accessSubdivision34
    virtual void releaseSubdivision34(
	    const Subdivision34 *subdiv34);

    /// \brief Elliptical texture filtering.
    /// \param color result color
    /// \param state current rendering state
    /// \param tex tag of database element miSCENE_IMAGE (the texture)
    /// \param remap reference to derived class Mip_remap providing
    /// implementation of texture coordinate transformation and remapping
    /// \param coord 2d texture coordinates (only x and y used).
    /// \return returns true on success, false if for example the input
    /// texture does not have the type miSCENE_IMAGE.
    virtual bool lookup_filter_color_texture(
	    miColor * const	color,
	    miState * const	state,
	    const miTag		tex,
	    Mip_remap &		remap,
	    miVector *		coord);

    /// \brief Open an output image from an output shader.
    /// \param image the returned image pointer
    /// \param state current rendering state
    /// \param idx the real index into the buffer array,
    /// retrieved from fb->get_index(buf_name, idx)
    /// \return returns true on success, false if the index is out of range,
    /// or this was not called from an output shader
    virtual bool open_output_image(
            miImg_image *       &image,
            miState *           state,
            const size_t        idx);

    /// \brief Close an output image from an output shader.
    /// \param state current rendering state
    /// \param idx the real index into the buffer array,
    /// retrieved from fb->get_index(buf_name, idx)
    /// \return returns true on success, false if the index is out of range,
    /// or this was not called from an output shader
    virtual bool close_output_image(
                miState *           state,
                const size_t        idx);


    /// Pass rendering related methods

    /// \brief get the current sample value
    /// \param state current rendering state
    /// \param idx framebuffer index to return value from
    /// \returns a pointer to the current sample value of the current
    /// sample possition of the framebuffer at index idx
    virtual const void* renderpass_get_cur_sample(
		miState *	state,
		const size_t	idx);

    /// \brief get the current pass sample value
    /// \param state current rendering state
    /// \param idx framebuffer index to return value from
    /// \returns a pointer to the sample value of the current pass
    /// of the current sample possition of the framebuffer at index idx
    virtual const void* renderpass_get_pass_sample(
		miState *	state,
		const size_t	idx);

    /// \brief set the new value for the current sample position
    /// \param state current rendering state
    /// \param idx framebuffer index to set the value in
    /// \param sample pointer to the sample value to set
    /// \returns true if the sample could be set false if there was an error
    virtual bool renderpass_set_sample(
		miState *	state,
		const size_t	idx,
		const void*	sample);

    /// \brief get the current pass number
    /// \param state current rendering state
    /// \returns the index number of the current rendering pass
    virtual size_t renderpass_get_pass_number(miState *state);

    /// \brief see description above.
    /// \param color result color
    /// \param state current rendering state
    /// \param tex tag of database element miSCENE_IMAGE (the texture)
    /// \param remap reference to derived class Mip_remap providing
    /// implementation of texture coordinate transformation and remapping
    /// \param coord 2d texture coordinates (only x and y used).
    /// \param ft specifies interpolation type for the lookup
    enum Filtertype {Bilinear, Bicubic};
    virtual bool lookup_filter_color_texture(
	    miColor * const	color,
	    miState * const	state,
	    const miTag		tex,
	    Mip_remap &		remap,
	    miVector *		coord,
	    Filtertype		ft);

    /// \brief Internal function to create a light list for multiple
    /// importance sampling (MIS).
    ///
    /// This may be used to generate light iterators for MIS. This method
    /// is needed by the MISLightIterator::MISLightIterator() constructor.
    /// Usually there is no need to invoke this method directly.
    /// \param state provided the method with the current rendering state. From
    /// the state the current instance light list may be deduced.
    /// \param slist is an optional list of light tags. If provided, this list
    /// will be used instead of the default instance light list.
    /// \param n gives the number of light tags in the optional light list.
    /// \return the method returns a pointer to a MISLightList.
    virtual MISLightList *createMISLightList(
	miState		*state,
	miTag 		*slist = 0,
	int 		n = 0);

    /// \brief Internal function to create a light list for multiple
    /// importance sampling (MIS).
    ///
    /// This may be used to generate light iterators for MIS. This method
    /// is needed by the MISLightIterator::MISLightIterator() constructor.
    /// Usually there is no need to invoke this method directly.
    /// \param state provided the method with the current rendering state. From
    /// the state the current instance light list may be deduced.
    /// \param bsdf is the BSDF to use.
    /// \param slist is an optional list of light tags. If provided, this list
    /// will be used instead of the default instance light list.
    /// \param n gives the number of light tags in the optional light list.
    /// \return the method returns a pointer to a MISLightList.
    virtual MISLightList *createMISLightList(
	miState		*state,
	Access_bsdf	&bsdf,
	miTag 		*slist = 0,
	int 		n = 0);

    /// \brief see description above.
	/// \param color result color
    /// \param state current rendering state
    /// \param tex tag of database element miSCENE_IMAGE (the texture)
    /// \param remap reference to derived class Mip_remap providing
    /// implementation of texture coordinate transformation and remapping
    /// \param coord 2d texture coordinates (only x and y used).
	/// \param ft specifies interpolation type for the lookup
    /// \param blur specifies blur factor for lookup, (1 = default, >1: blur)
    virtual bool lookup_filter_color_texture(
        miColor * const	color,
        miState * const	state,
        const miTag		tex,
        Mip_remap &		remap,
        miVector *		coord,
        Filtertype		ft,
        miScalar		blur);
};


/// \brief Access to string options.
///
/// Up to version 3.4, options are hardcoded in the struct miOptions in
/// shader.h. New options are implemented as arbitrary name - value pairs,
/// where the name of the option is an arbitrary string, and the value can be a
/// boolean, string, integration, float, 2, 3 or 4 floats.
///
/// A pointer to string options must be obtained with Interface::getOptions().
/// When the pointer is no longer needed then the Options::release() method
/// must be called, like for example:
/// \code
/// mi::shader::Interface *iface = mi_get_shader_interface();
/// mi::shader::Options *opt = iface->getOptions(string_options_tag);
/// iface->release();
/// opt->set("favorite color", "blue");
/// opt->release();
/// \endcode
/// 
/// <h3>Setting options</h3>
/// Set functions set the value of an option of a given name, overwriting any
/// previous value. Previous values may be overwritten by values of a different
/// type.
///
/// \note Options should only be set before rendering starts. It is undefined
/// which value will be used if an option is set during rendering.
///
/// <h3>Getting options</h3>
/// All get functions return true and set the value if a matching option is
/// found, or returns false leave the value unmodified if no matching option is
/// found.
///
/// <h3>Strings and memory management</h3>
/// Strings passed as arguments are completely controlled by the caller; mental
/// ray uses the strings briefly, or makes copies of the passed strings.
///
/// Strings returned by these functions are read-only and controlled by mental
/// ray. The caller may use these only for a short time and may not delete them.
/// Make a copy if the value is needed later.

class Options {
  public: 
    /// \{

    /// \brief Set a boolean option.
    /// \param name is the name of the option to set.
    /// \param value is the new value of the option.
    virtual void set(
	const char 	*name, 
	bool 		value) = 0;

    /// \brief Set a string option.
    /// \param name is the name of the option to set.
    /// \param value mental ray will make a copy of the passed string \a value,
    /// the passed argument is under control
    /// of the caller.
    virtual void set(
	const char 	*name, 
	const char *	value) = 0;

    /// \brief Set an integer option.
    ///\note Integer options may also be used as floating point values.
    /// \param name is the name of the option to set.
    /// \param value is the new value of the option.
    virtual void set(
	const char 	*name, 
	int 		value) = 0;

    /// \brief Set a floating point option.
    /// \param name is the name of the option to set.
    /// \param value is the new value of the option.
    virtual void set(
	const char 	*name, 
	float 		value) = 0;

    /// \brief Set a float double option.
    /// \param name is the name of the option to set.
    /// \param value1 is the first component of the double.
    /// \param value2 is the second component of the double.
    virtual void set(
	const char 	*name,
	float 		value1, 
	float 		value2) = 0;

    /// \brief Set a float triple option.
    /// \param name is the name of the option to set.
    /// \param value1 is the first component of the triple.
    /// \param value2 is the second component of the triple.
    /// \param value3 is the third component of the triple.
    virtual void set(
	const char 	*name,
	float 		value1, 
	float 		value2, 
	float 		value3) = 0;

    /// \brief Set a float quadruple option.
    /// \param name is the name of the option to set.
    /// \param value1 is the first component of the quadruple.
    /// \param value2 is the second component of the quadruple.
    /// \param value3 is the third component of the quadruple.
    /// \param value4 is the third component of the quadruple.
    virtual void set(
	const char 	*name, 
	float 		value1, 
	float 		value2, 
	float 		value3, 
	float 		value4) = 0;

    /// \brief Get a boolean option.
    /// \param name is the name of the option to look up
    /// \param value will be set on success, and left unchanged otherwise.
    /// \return true if an option of the given name and type is found, false
    /// otherwise.
    virtual bool get(
	const char 	*name, 
	bool 		*value) const = 0;

    /// \brief Get a string option.
    /// \param name is the name of the option to look up
    /// \param value The returned string \a value is only value for a short
    /// time, and may not be modified or deleted by the caller. The caller
    /// should make a copy of the string if needed.
    /// \return true if an option of the given name and type is found, false
    /// otherwise.
    virtual bool get(
	const char 	*name, 
	const char 	**value) const = 0;

    /// \brief Get an integer option.
    /// \param name is the name of the option to look up
    /// \param value will be set on success, and left unchanged otherwise.
    /// \return true if an option of the given name and type is found, false
    /// otherwise.
    virtual bool get(
	const char 	*name, 
	int 		*value) const = 0;

    /// \brief Get a floating point option.
    ///
    /// If the value of the named option is an integer then the integer is
    /// converted to a floating point number and returned in \a value.
    /// \param name is the name of the option to look up
    /// \param value will be set on success, and left unchanged otherwise.
    /// \return true if an option of the given name and type is found, false
    /// otherwise.
    virtual bool get(
	const char 	*name, 
	float 		*value) const = 0;

    /// \brief Get a floating point double option.
    ///
    /// This can be used for 2 dimensional vectors.
    /// \param name is the name of the option to look up
    /// \param value1 will be set to the first component on success, and left
    /// unchanged otherwise.
    /// \param value2 will be set to the second component on success, and left
    /// unchanged otherwise.
    /// \return true if an option of the given name and type is found, false
    /// otherwise.
    virtual bool get(
	const char 	*name, 
	float 		*value1, 
	float 		*value2) const = 0;

    /// \brief Get a floating point triple option.
    ///
    /// This can be used for RGB colors or 3 dimensional vectors.
    /// \param name is the name of the option to look up
    /// \param value1 will be set to the first component on success, and left
    /// unchanged otherwise.
    /// \param value2 will be set to the second component on success, and left
    /// unchanged otherwise.
    /// \param value3 will be set to the third component on success, and left
    /// unchanged otherwise.
    /// \return true if an option of the given name and type is found, false
    /// otherwise.
    virtual bool get(
	const char 	*name, 
	float 		*value1, 
	float 		*value2, 
	float 		*value3) const = 0;

    /// \brief Get a floating point quadruple option.
    ///
    /// This can be used for RGBA colors or 4 dimensional homogenous vectors.
    /// \param name is the name of the option to look up
    /// \param value1 will be set to the first component on success, and left 
    /// unchanged otherwise.
    /// \param value2 will be set to the second component on success, and left 
    /// unchanged otherwise.
    /// \param value3 will be set to the third component on success, and left 
    /// unchanged otherwise.
    /// \param value4 will be set to the fourth component on success, and left 
    /// unchanged otherwise.
    /// \return true if an option of the given name and type is found, false 
    /// otherwise.
    virtual bool get(
	const char	*name,
	float 		*value1,
	float 		*value2,
	float 		*value3,
	float 		*value4) const = 0;

    /// \brief Delete a specific option.
    ///
    /// This can be used to remove unneeded options. 
    /// \return true if an option of the given name and type is found, false 
    /// otherwise. 
    virtual bool remove(
	const char	*name) = 0;

    /// \brief Release (delete) the interface.
    ///
    /// This should be called when done. It may release the Options object.
    virtual void release() = 0;
};



/// \brief Interface wrapper class
///
class Access_interface {
public:
    /// \brief constructor
    Access_interface(int version = mi_ray_interface_version)
	: m_iface (mi_get_shader_interface(version))
    {}

    /// \brief destructor
    ~Access_interface()
    {
	m_iface->release();
	m_iface = 0;
    }

    /// \brief dereference operator
    mi::shader_v3::Interface * operator->()
    {
	return m_iface;
    }

private:
    mi::shader_v3::Interface *m_iface;
};


/// \brief Typedef for backwards compatibility.
///
/// \deprecated Replaced by \c Access_interface.
typedef Access_interface Interface_access;


} // namespace shader_v3


// namespace alias, shaders should use it
namespace shader = shader_v3;

} // namespace mi

#include "shader_framebuffer.h"
#include "shader_output.h"
#include "shader_map.h"
#include "shader_lightlist.h"
#include "shader_sds34.h"
#include "shader_mipremap.h"
#include "shader_importance.h"

#endif // MI_SHADER_IF_H
